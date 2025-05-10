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
All dependencies are automatically installed by running `Install-Dependencies.py`

## 🚀 Setup Instructions

1. Download the repository to your local machine.
2. Run the `Run-All.py` script
3. If not already present, a window will appear and ask you to fill some variables for the `.env` file
   - Variables:
     - **Player** : The chess.com username to analyze
     - **Games to Review** : Integer for how many of the latest games to analyze (Use `-1` analyze all)
     - **Bot username** & **Bot password** : Username and password of a bot account that will be used to scrape through your games. (Any account that uses chess.com's own login page, even yours)
   - **NOTE:** It will only generate the `.env` once. To redo, it you can manually edit or delete it (You will be asked to fill the variables again) 
4. The program will analyze your games and automatically open the results in your default browser when it's done! 🖥️🎉

**NOTE:** Whilst the program is running, it will open a browser and open the games sequentially. This is essential, **DO NOT INTERRUPT IT!!**

## Why not create a workflow?
A GitHub Runner has only 2 cores meaning that results using a GitHub workflow will be much less accurate then running it locally on one's own computer.
