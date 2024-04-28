import requests
from colorama import Fore
import os
import zipfile
import time
from datetime import datetime
import psutil

import wget
VERSION = 1.1
# Color
RESET = Fore.RESET
RED = Fore.LIGHTRED_EX
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE1 = Fore.LIGHTBLUE_EX
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
EX = Fore.LIGHTMAGENTA_EX

# Error 

def process(name):
    for proc in psutil.process_iter():
        if name.lower() == proc.name().lower():
            return True
    else:
        return False


def step(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{EX}STEP{RESET}] : {m}")
    return
def error(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{RED}ERROR{RESET}] : {m}")
    return

def success(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{GREEN}SUCCESS{RESET}] : {m}")
    return

def warn(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{YELLOW}WARNING{RESET}] : {m}")
    return

def info(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{CYAN}INFO{RESET}] : {m}")
    return

def load(m):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print(f"[{BLUE}{currentTime}{RESET}] ==> [{CYAN}LOADING{RESET}] : {m}")
    return

def mainwindows():
    try:
        os.system("cls")
        try:
            r = requests.get(f"https://api.cmoidylan.xyz/logo")
        except requests.ConnectTimeout:
            error("Connection Timeout")
            time.sleep(5)
            os._exit(1)
        print(f"{BLUE}{r.text}{RESET}")
        info(f"You are using the ver-{VERSION}")
        step("Checking for update...")
        time.sleep(5)
        r = requests.get(f"https://api.cmoidylan.xyz/version?ver={VERSION}")
        if r.json()["status"] == True or "True":
            success("No update available")
            pass
        else:
            warn("New update available")
            os.system("start https://github.com/cmoidylan/KrampDown")
            time.sleep(5)
            os._exit(1)
        if os.path.exists("temp"):
            pass
        else:
            os.mkdir("temp")
            warn("If the program does not work, try creating the temp folder yourself in the folder where KrampDown.exe is located")
        if process("RobloxPlayerBeta.exe") or process("Bloxstrap.exe") or process("RobloxStudioBeta.exe"):
            warn("Roblox is running")
            step("Stopping Roblox...")
            os.system("taskkill /f /im RobloxPlayerBeta.exe")
            os.system("taskkill /f /im RobloxStudioBeta.exe")
            os.system("taskkill /f /im Bloxstrap.exe")
            time.sleep(5)
            pass
        else:
            pass
        
        try:
            r = requests.get(f"https://api.cmoidylan.xyz/logo")
        except requests.ConnectTimeout:
            error("Connection Timeout")
            time.sleep(5)
            os._exit(1)
        print("1. Downgrade \n2. Revert")
        x = input("==> ")
        if x == "1":
            os.system("cls")
            print(f"{BLUE}{r.text}{RESET}")
            step("Checking your Roblox Versions...")
            folder_names = os.listdir(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions")
            folders = [f for f in folder_names if os.path.isdir(os.path.join(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions", f))]
            info(f"You are using the Roblox Version : {folders[0]}")
            step("Check compatibility...")
            try:
                r = requests.get("https://clientsettings.roblox.com/v2/client-version/WindowsPlayer")
            except requests.ConnectTimeout:
                error("Connection Timeout")
                time.sleep(5)
                os._exit(1)
            if r.json()["clientVersionUpload"] == folders[0] or f"{folders[0]}":
                success("Your version is compatible !")
            else:
                warn("Your version is not compatible !")
                os.system(f"start C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Bloxstrap.exe")
                info("Restart the program after BloxStrap has updated your Roblox.")
                time.sleep(5)
                os._exit(1)
            step("Downgrading...")
            info("Downloading Roblox...")
            try:
                r = requests.get("https://api.cmoidylan.xyz/clientdowngradeversion")
            except requests.ConnectTimeout:
                error("Connection Timeout")
                time.sleep(5)
                os._exit(1)
            open('temp/version.zip', 'wb').write(r.content)
            info("Unzipping ...")
            with zipfile.ZipFile("temp/version.zip", "r") as zip_ref:
                zip_ref.extractall(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions/{folders[0]}")
            info("Cleaning up...")
            x = open(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/r.rdown", "+w")
            x.write("DO NOT DELETE THIS FILE")
            x.close()
            os.remove("temp/version.zip")
            success("Downgrade complete")
            info("Press enter to start Bloxstrap")
            os.system("pause")
            os.system(f"start C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Bloxstrap.exe")
            info("Bloxstrap Started...")
            time.sleep(5)
            mainwindows()
        if x == "2":
            if os.path.exists(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/r.rdown"):
                folder_names = os.listdir(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions")
                folders = [f for f in folder_names if os.path.isdir(os.path.join(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions", f))]
                os.remove(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/r.rdown")
                os.rename(f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions/{folders[0]}", f"C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Versions/version-492b7f0827474659")
                success("Revert complete")
                info("Press enter to start Bloxstrap")
                os.system("pause")
                os.system(f"start C:/Users/{os.getlogin()}/AppData/Local/Bloxstrap/Bloxstrap.exe")
                info("Bloxstrap Started...")
                time.sleep(5)
                mainwindows()
            else:
                error("You have not downgraded your version")
                info("Please rerun the program and press 1 to downgrade your version")
                os.system("pause")
                os._exit(1)






        

    except KeyboardInterrupt:
        error("KeyboardInterrupt")
        time.sleep(5)
        os._exit(1)
mainwindows()
