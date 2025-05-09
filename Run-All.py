import os
import subprocess
import webbrowser

env = os.environ.copy()

subprocess.run(["python", "src/Collector.py"], env=env)
subprocess.run(["python", "src/Analyzer.py"], env=env)
subprocess.run(["python", "src/Summary.py"], env=env)

html_file = os.path.abspath("Results.html")
webbrowser.open(f"file://{html_file}")
