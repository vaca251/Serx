import os
import fnmatch
from colorama import init,  Fore
init(autoreset=True)
logotip = [
    Fore.GREEN + "███████╗███████╗██████╗ ██╗  ██╗",
    Fore.GREEN + "██╔════╝██╔════╝██╔══██╗╚██╗██╔╝",
    Fore.GREEN + "███████╗█████╗  ██████╔╝ ╚███╔╝ ",
    Fore.GREEN + "╚════██║██╔══╝  ██╔══██╗ ██╔██╗ ",
    Fore.GREEN + "███████║███████╗██║  ██║██╔╝ ██╗",
    Fore.GREEN + "╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝",
    Fore.GREEN + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
]
for x in logotip:
    print(x)
def search_file(pattern, path):
    try:
        found = False
        for root, dirs, files in os.walk(path):
            for name in dirs + files:
                if fnmatch.fnmatch(name, pattern):
                    full_path = os.path.join(root, name)
                    print(f"Found: {full_path}")
                    found = True
        if not found:
            print("No files or folders matched the pattern.")
    except Exception as e:
        print(f"Error: {e}")
while True:
    try:
        pattern = input("Enter file/folder name or pattern: ")
        path = input("Enter path to search for file/folder: ")
        search_file(pattern, path)
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("")
        exit()