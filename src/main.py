import discord
from discord.ext import commands
import json
import dotenv
import os
import random
import re
import sys

class MissingRequiredParameter(Exception):
    pass

class NoResult(Exception):
    pass

filename = "jsoncord.json"
try:
    filename = sys.argv[1]
except:
    print("You must enter a file name ex: python main.py <file name>")
    sys.exit()

<<<<<<< HEAD
with open(f"{filename}", 'r') as f:
=======
with open(f"../{filename}", 'r') as f:
>>>>>>> 06a4bc102606f21403f84366c0f7485ab7b3268c
    _file = json.load(f)['bot']

try:
    _bot_token = _file['token']
    if _bot_token.startswith("readEnv:"):
        envName = _bot_token.split(" ")[1]
        dotenv.load_dotenv()
        try:
            _bot_token = os.getenv(envName)
        except Exception as e:
            print("Environment Error: {}".format(e))
            sys.exit()

except KeyError:
    raise MissingRequiredParameter("Token is missing in your JSON file")
    sys.exit()
try:
    _bot_prefix = _file['prefix']
except KeyError:
    raise MissingRequiredParameter("Prefix is missing in your JSON file")
    sys.exit()
try:
    _bot_commands = _file['commands']
except:
    raise MissingRequiredParameter("Commands is missing in your JSON file")
    sys.exit()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=_bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print("Your bot is ready")

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
    elif text.startswith("%random.random"):
        return random.random()
    elif text.startswith("%message.author.name"):
        return message.author.name
    elif text.startswith("%message.author.id"):
        return message.author.id
    elif text.startswith("%message.author.mention"):
        return message.author.mention
    elif text.startswith("%getMessageArg"):
        return message.content.split(" ")[int(arg[0]) + 1]
    else:
        pass

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

def _compile_variable(text:str, commands:dict, message: discord.Message):
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

async def trigger(message: discord.Message, commands:dict, response):
    if response['name'] == "sendMessage":
        try:
<<<<<<< HEAD
            await message.channel.send(_compile_variable(response['value'], commands, message))
        except Exception as e:
            print(e)
=======
            await message.channel.send(response['value'])
        except Exception as e:
            pass
    elif response['name'] == "banMember":
        try:
            await message.guild.ban(response['userID'], reason=response['reason'])
        except:
            pass
>>>>>>> 06a4bc102606f21403f84366c0f7485ab7b3268c
    else:
        raise NoResult("Trigger {} not found! Try read the documentation at https://github.com/yeahbois/jsoncord/readme.md".format(response['name']))
        sys.exit()

@bot.event
async def on_message(message):
    for commands in _bot_commands:
        if message.content.lower().startswith(f"{_bot_prefix}{commands['name']}") or message.content.lower().startswith(f"{_bot_prefix} {commands['name']}"):
            for response in commands['trigger']:
                await trigger(message, commands, response)
        else:
            pass


bot.run(_bot_token)