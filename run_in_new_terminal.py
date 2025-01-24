# run_in_new_terminal.py

import subprocess
import os
import sys

def run_script_in_new_terminal(script_name, file_path):
    if os.name == 'nt':  # Windows
        command = f'start cmd /k "python {script_name} {file_path} & exit"'
        subprocess.run(command, shell=True)
    elif os.name == 'posix':  # Unix-like systems (Linux, MacOS)
        command = f'gnome-terminal -- bash -c "python3 {script_name} {file_path}; exec bash"'
        subprocess.run(command, shell=True)
    else:
        print(f"Unsupported OS: {os.name}")

if len(sys.argv) != 3:
    print("Usage: python run_in_new_terminal.py <script_name> <file_path>")
else:
    script_name = sys.argv[1]
    file_path = sys.argv[2]
    run_script_in_new_terminal(script_name, file_path)
