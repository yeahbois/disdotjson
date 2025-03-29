# Dis.json

## 📌 Read the [Installation Guide](https://github.com/yeahbois/disdotjson/blob/master/howtoinstall.md)
A **Discord Bot** configured entirely in **JSON**, powered by the `pycord` module.

---

## 🚀 Update Log
### 🔹 Version: `1.0`
### 📅 Release Date: `16/06/2022`
### 📜 Changelog:
- 🆕 Initial release

---

## 🔧 How to Use?
Create a JSON configuration file:

```json
{
    "bot": {
        "token": "Your token here",
        "prefix": "?",
        "commands": []
    }
}
```

### 🔑 Key Parameters
- **`token`**: Your bot token. You can also use an environment variable with `readEnv: <environment name>`.
- **`prefix`**: The bot's command prefix.
- **`commands`**: A list of configured commands.

---

## 📜 Commands Format
Each command inside the `commands` list must be an object with the following format:

```json
{
    "name": "command name", 
    "trigger": [], 
    "variables": {}
}
```

### 🔥 Triggers
Triggers define how the bot responds. A command object must include one or more trigger keys.

#### 🎯 Trigger Types
- **`sendMessage`**: Sends a message. 
  - **Parameter**: `value` – The message text (supports variables using `$variable_name`).
- **`else`**: More details in the full documentation.

### 📌 Variables
Variables store reusable values that can be used inside messages or scripts.

```json
"variables": {
    "$variablename": "text, script, or scriptv2"
}
```

#### 🔹 Variable Types
- **`text`**: Plain text.
- **`script`**: Uses functions, formatted as `script: %function(parameters)`, replacing the variable with the function result.
- **`scriptv2`**: Supports multiple functions in one variable.

#### 📍 Example Usage
- **`scriptv2`**:
  ```json
  "$variablename": "scriptv2: %user.name is cool, %user.mention"
  ```
- **`script`**:
  ```json
  "$variablename": "script: %user.name"
  ```

---

# ⚡ Available Functions

## 🎲 Random
- **`random.number(from, to)`** → Returns a random number.
  ```
  %random.number(1, 100)
  ```
- **`random.string(choices)`** → Returns a random choice.
  ```
  %random.string(choice1; choice2; choice3)
  ```
- **`random.random()`** → Returns a random float.
  ```
  %random.random()
  ```

## 🔡 String Manipulation
- **`string.lower(text)`** → Converts text to lowercase.
  ```
  %string.lower(HeLLo) → hello
  ```
- **`string.upper(text)`** → Converts text to uppercase.
  ```
  %string.upper(hello) → HELLO
  ```
- **`string.capitalize(text)`** → Capitalizes the text.
  ```
  %string.capitalize(hello world) → Hello world
  ```

## 📩 Message
- **`message.getArg(index)`** → Returns the nth argument of a command.
  ```
  %message.getArg(1)
  ```
- **`message.author.name()`** → Returns the author's name.
  ```
  %message.author.name()
  ```
- **`message.author.id()`** → Returns the author's ID.
  ```
  %message.author.id()
  ```
- **`message.author.mention()`** → Mentions the author.
  ```
  %message.author.mention()
  ```
- **`message.author.avatarUrl()`** → Returns the author's avatar URL.
  ```
  %message.author.avatarUrl()
  ```

## ⏳ Time
- **`time.unix()`** → Returns the current UNIX timestamp.
  ```
  %time.unix()
  ```

## 🧮 Math
- **`math.count(expression)`** → Evaluates a mathematical expression.
  ```
  %math.count(1 + 2 * 3)
  ```

## 🌍 Requests
- **`requests.get.json(url, key)`** → Fetches JSON data from an API.
  ```
  %requests.get.json(https://api.example.com/data, result)
  ```
- **`requests.get.text(url)`** → Fetches text data from an API.
  ```
  %requests.get.text(https://api.example.com/data)
  ```

## ✅ Check Functions
- **`check.string(value)`** → Checks if a value is a string.
  ```
  %check.string(1234) → false
  ```
- **`check.integer(value)`** → Checks if a value is an integer.
  ```
  %check.integer(1234) → true
  ```

---

## ⚡ Trigger Types (Coming Soon!)
