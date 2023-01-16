#                 READ LISENCE FILE                     #
#                Dis.json version 1.0                   #

'''
Imports

Required:
READ requirements.txt
'''
import discord
from discord.ext import commands
import json
import dotenv
import os
import random
import re
import sys
import time
import requests
import errors
import functions

'''
Get JSON file and the content
'''
try:
    filename = sys.argv[1]
except:
    raise errors.MissingRequiredParameter("You must enter the json file directory")

with open(f"{filename}", 'r') as f:
    _file = json.load(f)['bot']

'''
Get the bot required parameter
- Token
- Prefix
- Commands
'''
try:
    _bot_token = _file['token']
    if _bot_token.startswith("readEnv:"):
        envName = _bot_token.split(" ")[1]
        dotenv.load_dotenv()
        try:
            _bot_token = os.getenv(envName)
        except Exception as e:
            raise errors.SystemError("Error in environment: {}".format(e))
except KeyError:
    raise errors.MissingRequiredParameter("Token is missing in your JSON file")
try:
    _bot_prefix = _file['prefix']
except KeyError:
    raise errors.MissingRequiredParameter("Prefix is missing in your JSON file")
try:
    _bot_commands = _file['commands']
except:
    raise errors.MissingRequiredParameter("Commands is missing in your JSON file")

'''
Creating the client using py-cord
'''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=_bot_prefix, intents=intents)

'''
Functions
'''
def _compile_variable(text:str, commands:dict, message: discord.Message):
    def _compile_scriptv1(text, commands:dict, message: discord.Message):
        text = text.replace("script:", "")
        textAlf = []
        for item in list(text):
            textAlf.append(item)
        if textAlf[0] == " ":
            textAlf.pop(0)
        text = "".join(textAlf)
        result = _compile_function(text, commands, message)
        return result

    def _compile_scriptv2(text, commands:dict, message: discord.Message):
        text = text.replace("scriptv2:", "")
        textAlf = []
        for item in list(text):
            textAlf.append(item)
        if textAlf[0] == " ":
            textAlf.pop(0)
        text = "".join(textAlf)
        splitted = text.split(" ")
        for texts in splitted:
            if texts.startswith("%"):
                result = _compile_function(texts, commands, message)
                splitted[splitted.index(texts)] = result
        return " ".join(splitted)
    splitted = text.split(" ")
    for texts in splitted:
        if texts.startswith("$"):
            commandsIndex = _file['commands'].index(commands)
            vars = _file['commands'][commandsIndex]['variables']
            try:
                varResult = vars[texts]
                if varResult.startswith("script:"):
                    _result = str(_compile_scriptv1(varResult, commands, message))
                elif varResult.startswith("scriptv2:"):
                    _result = str(_compile_scriptv2(varResult, commands, message))
                else:
                    _result = varResult
                splitted[splitted.index(texts)] = str(_result)
            except:
                pass

    return " ".join(splitted)

def _compile_function(text:str, commands:dict, message: discord.Message):
    arguments = re.findall(r'\(.*?\)', text)
    argList = []
    for argAlf in list(arguments[0]):
        argList.append(argAlf)
    if argList[0] == "(":
        argList.pop(0)
    if argList[len(argList) - 1] == ")":
        argList.pop(len(argList) - 1)
    arguments = "".join(argList)
    arg = arguments.split(";")
    if text.startswith("%random.number"):
        return random.randint(int(arg[0]), int(arg[1]))
    elif text.startswith("%random.string"):
        return random.choice(arg)
    elif text.startswith("%string.lower"):
        return arg[0].lower()
    elif text.startswith("%string.upper"):
        return arg[0].upper()
    elif text.startswith("%string.capitalize"):
        return arg[0].capitalize()
    elif text.startswith("%random.random"):
        return random.random()
    elif text.startswith("%message.author.name"):
        return message.author.name
    elif text.startswith("%message.author.id"):
        return message.author.id
    elif text.startswith("%message.author.mention"):
        return message.author.mention
    elif text.startswith("%message.author.avatarUrl"):
        return message.author.avatar.url
    elif text.startswith("%message.getArg"):
        return message.content.split(" ")[int(arg[0]) + 1]
    elif text.startswith("%time.unix"):
        return time.time()
    elif text.startswith("%math.count"):
        values = list(arg[0])
        whitelist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "^", ".", "(", ")", " ", ","]
        inputList = []
        for alf in values:
            if alf in whitelist:
                inputList.append(alf)
            else:
                raise errors.SystemError("Invalid character in math.count()")
        return eval("".join(inputList))
    elif text.startswith("%requests.get.json"):
        if not arg[0]:
            raise errors.MissingRequiredParameter("Missing url in %requests.get()")
        if not arg[1]:
            return requests.get(arg[0]).json()
        else:
            return requests.get(arg[0]).json()[arg[1]]
    elif text.startswith("%requests.get.text"):
        if not arg[0]:
            raise errors.MissingRequiredParameter("Missing url in %requests.get()")
        return requests.get(arg[0]).text
    elif text.startswith("%check.integer"):
        if arg[0].isdigit():
            return "true"
        else:
            return "false"
    elif text.startswith("%check.string"):
        if arg[0].isalpha():
            return "true"
        else:
            return "false"
    else:
        pass

async def trigger(message: discord.Message, commands:dict, response):
    if response['name'] == "sendMessage":
        try:
            await message.channel.send(_compile_variable(response['value'], commands, message))
        except Exception as e:
            print(e)
    else:
        raise errors.NoResult("Trigger {} not found! Try read the documentation at https://github.com/yeahbois/disdotjson/blob/master/README.md".format(response['name']))

@bot.event
async def on_ready():
    print("Your bot is ready")
    print(f'''
Name: {bot.user.name}#{bot.user.discriminator}
ID: {bot.user.id}
Command Count: {len(_file['commands'])}
    ''')

@bot.event
async def on_message(message):
    for commands in _bot_commands:
        if message.content.lower().startswith(f"{_bot_prefix}{commands['name']}") or message.content.lower().startswith(f"{_bot_prefix} {commands['name']}"):
            for response in commands['trigger']:
                await trigger(message, commands, response)
        else:
            pass

bot.run(_bot_token)