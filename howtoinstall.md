# How to Install Dis.json ?

## 1. Download this project
- Click Green "Code:" button
- Download zip
- Extract Zip

## 2. Create a JSON file as the main file

## 3. Run using:
```sh
python3 src/main.py (your json file directory)
```

### You can also use a batch file:
1. Create `run.bat` file
2. Fill it with this code:
```bat
python3 src/main.py (your json file directory)
```
3. Run it using:
```sh
run
```

---

# I Get an Error

## "python3 is not a command"
- Check if Python is installed and added to the system environment variables.
- Try replacing `python3` with `py` or `python`.

## "Module not found"
- You must install the missing module using:
```sh
pip install <module_name>
```
- If you get an error like "pip is not recognized" or "pip is not a command", install pip.
  - You can find tutorials on YouTube or Google.
