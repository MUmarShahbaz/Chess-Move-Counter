import subprocess
import sys

def run_command(command):
    """Run a subprocess command and stream output live to console."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        print(line, end='')

    process.wait()
    if process.returncode != 0:
        print(f"❌ Command failed: {' '.join(command)}")
    else:
        print(f"✅ Command succeeded: {' '.join(command)}")

print("Installing pip packages...")
run_command([sys.executable, "-m", "pip", "install", "dotenv", "requests", "playwright"])

print("\nInstalling Playwright browser (chromium)...")
run_command([sys.executable, "-m", "playwright", "install", "chromium"])