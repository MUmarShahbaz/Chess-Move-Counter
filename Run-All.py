import os
import subprocess
import webbrowser
from dotenv import load_dotenv
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
import sys

if sys.platform == "win32":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass


if not os.path.exists(".env"):
    def save_env():
        with open(".env", "w") as f:
            f.write(f"PLAYER={player.get()}\n")
            f.write(f"NUMBER_TO_REVIEW={n.get()}\n")
            f.write(f"BOT_USER={b_user.get()}\n")
            f.write(f"BOT_PASS={b_pass.get()}\n")
        messagebox.showinfo("Success", ".env file created!")
        root.destroy()

    root = Tk()
    root.title(".env File Generator")

    Label(root, text="Player:").grid(row=0, column=0, sticky="e")
    Label(root, text="Games to Review:").grid(row=1, column=0, sticky="e")
    Label(root, text="Bot Username:").grid(row=2, column=0, sticky="e")
    Label(root, text="Bot Password:").grid(row=3, column=0, sticky="e")

    player = StringVar()
    n = StringVar(value=-1)
    b_user = StringVar()
    b_pass = StringVar()

    Entry(root, textvariable=player, width=40).grid(row=0, column=1)
    Entry(root, textvariable=n, width=40).grid(row=1, column=1)
    Entry(root, textvariable=b_user, width=40).grid(row=2, column=1)
    Entry(root, textvariable=b_pass, width=40).grid(row=3, column=1)

    Button(root, text="Generate .env", command=save_env).grid(row=4, columnspan=2, pady=10)

    root.mainloop()

load_dotenv()
env = os.environ.copy()

subprocess.run(["python", "src/Collector.py"], env=env)
subprocess.run(["python", "src/Analyzer.py"], env=env)
subprocess.run(["python", "src/Summary.py"], env=env)

html_file = os.path.abspath("Results.html")
webbrowser.open(f"file://{html_file}")
