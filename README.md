# ♟️ Chess Move Counter

**Chess Move Counter** is a Python-based tool that analyzes your previously reviewed games and counts **every single type of move** you've made.

## ✨ Features

- 🤖 Automatically scrapes through already reviewed chess games
- 📊 Categorizes and counts all move types
- 🌐 Opens the results in your default web browser automatically

## 📤 Example Output
<div align="center"><img width="400px" height="auto" src="https://github.com/user-attachments/assets/16a15f2a-7164-424e-af04-e645ae4027be"></div>

## 🛠️ Prerequisites

Before you get started, make sure you have:

- 🐍 [Python](https://www.python.org/)
- 🧠 [Visual Studio Code](https://code.visualstudio.com/)
- 🧩 [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 🔧 Dependencies
- 📦 Python packages:
  - `requests`
  - `playwright` with `chromium`

To install dependencies:
```bash  
pip install requests playwright  
playwright install chromium  
```

## 🚀 Setup Instructions

1. Download the repository to your local machine.
2. In VS Code, create a `.env` file in the root directory
3. Add the following to the `.env`:
   ```env
   PLAYER=Your_Username
   NUMBER_TO_REVIEW=10
   BOT_USER=Bot_Username
   BOT_PASS=Bot_Password
   ```
   - `PLAYER` : The chess.com username to analyze
   - `NUMBER_TO_REVIEW` : Integer for how many of the latest games to analyze (Use `-1` analyze all)
   - `BOT_USER` & `BOT_PASS` : username and password of a bot account that will be used to scrape through your games. (You can use your own account instead of making a bot)
4. Open the VS Code debugger and run the `Run All` configuration.
5. The program will analyze your games and automatically open the results in your default browser when it's done! 🖥️🎉

**NOTE: WHILST THE PROGRAM IS RUNNING, IT WILL OPEN A BROWSER AND OPEN THE GAMES SEQUENTIALLY. THIS IS ESSENTIAL, DO NOT INTERUPT IT!!**

## Why not create a workflow?
A GitHub Runner has only 2 cores meaning that results using a GitHub workflow will be much less accurate then running it locally on one's own computer.
