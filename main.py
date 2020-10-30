import os, sys
from os import path

import subprocess

try:
    program_name = sys.argv[1]
    if program_name.strip() == ".":
        program_name = os.getcwd()
except IndexError:
    program_name = os.getcwd()

possible_paths = [r"C:\Program Files", r"C:\Program Files (x86)", r"C:\Users\Appu\AppData\Roaming", r"C:\Users\Appu\AppData\Local", r"C:\Users\Appu\AppData\LocalLow", r"D:\Programas"]
found = False

for position, current_path in enumerate(possible_paths):
    folder = path.join(current_path, path.split(program_name)[1])
    if path.exists(folder):
        subprocess.Popen(r'explorer /select, ' + folder)
        if not found:
            found = True

if not found:
    print(f"Folder [{folder}] was not found")
