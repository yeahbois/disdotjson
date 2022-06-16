# Dis.json
## Read the [how to install](https://github.com/yeahbois/dis.json/howtoinstall.md)
Discord Bot but in JSON. Writen in pycord module

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
Coming Soon

# Trigger Types
Coming Soon