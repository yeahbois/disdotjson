# Dis.json
## Read the [how to install](https://github.com/yeahbois/disdotjson/blob/master/howtoinstall.md)
Discord Bot but in JSON. Writen in pycord module

## Update!
### Version: 1.0
### Date: 16/06/2022
### Changelog:
#### - Initial release

## How to use ?
Create a JSON file
```json
{
    "bot": {
        "token": "Your token here",
        "prefix": "?",
        "commands": []
    }
}
```

### Keys
In the "bot" keys you must enter a object valued by:
- **Token**: You must enter your bot token. You can use read env too! by using `readEnv: <environment name>` as the token value
- **Prefix**: Here is your bot prefix
- **Commands**: A list that valued by the commands

#### Commands
Inside the "commands" key you must enter a list valued by a object
```json
{"name": "command name", "trigger": [], "variables": {}}
```
##### Trigger
To do something, you must enter a trigger keys inside the commands object
###### Trigger Type
- **sendMessage**: You can send message with it.
    Parameter:
        - value: The message, you can use variable with `$variable_name`
- **else**: Read the documentation at the bottom of this readme
##### Variables
The variables are a script or text that will replace the message
```json
"variables": {
    "$variablename": "text, script, or scriptv2"
}
```
###### Variables Type
- **text**
- **script**:
How to use? As a value, you can enter it with `script: %function(parameters)`. It will replace the variable in message with the function result
- **scriptv2**:
What is the difference? The difference between script and scriptv2 just, script can only run 1 function but scriptv2 can run more function
###### Example
- **scriptv2**
```json
"$variablename": "scriptv2: %user.name is cool, %user.mention"
```
- **script**
```json
"$variablename": "script": "%user.name"
```
# Functions
## Random
### - number(from:integer; to:integer)
#### Return a random number
#### %random.number(1, 100)

### - string(choices)
#### Return a random text
#### %random.string(choice1; choice2; choice3; untilInfinity)

### - random()
#### Return a random float
#### %random.random()

## String
### - lower(text:string)
#### Return the text but in lower
#### %string.lower(mY sTrInG) | out: my string 

### - upper(text:string)
#### Return the text but in upper
#### %string.upper(my string) | out: MY STRING

### - capitalize(text:string)
#### Return the text but in capitalize
#### %string.capitalize(my string) | out: My string

## Message
### - getArg(index:integer)
### Return the argument using the index
### %message.getArg(1)

### - author.name()
### Return the author name
### %message.author.name()

### - author.id()
### Return the author id
### %message.author.id()

### - author.mention()
### Return the author mention
### %message.author.mention()

### - author.avatarUrl()
### Return the author avatar url
### %message.author.avatarUrl()

## Time
### - unix()
### Return the unix time (how many seconds from `00:00:00 UTC January 1 1970`)
### %time.unix()

## Math
### - count(math)
### Count math
### %math.count(1 + 6 * 65 ^ 3/4 ** (12.3 / 0.1) - 1 // 70)

## Requests
### - get.json(url; key)
### Make a request and get the json result
### %requests.get.json(https://myapi.com/api?key=yes; result)

### - get.text(url)
### Make a request and get the text result
### %requests.get.text(https://myapi.com/api?key=yes)

## Check
### - string(something)
### Check if the argument are string. It will return true or false
### %check.string(1232) | out: false

### - integer(something)
### Check if the argument are integer. It will return true or false
### %check.integer(1234) | out: true

# Trigger Types
Coming Soon