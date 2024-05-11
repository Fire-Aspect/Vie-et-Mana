
from keyPressing import PressKey
from screenShotMaker import MakeScreenShot, DeleteScreenShot
from colorChecker import GetPixelColor
import time
import threading
import pythoncom
from interface import interface
import psutil
import queue

#r19 v80 b160
#r101 v11, b20

active = False
healthPotionTime = 5
manaPotionTime = 5

def OhShitGiveMeHealth():
    pythoncom.CoInitialize()
    print("auto health started")
    try:
        while True:
            if not active:
                continue
            time.sleep(0.6)
            MakeScreenShot("health")
            if GetPixelColor("health") != (101, 11, 20):
                PressKey("&")
                DeleteScreenShot("health")
                time.sleep(healthPotionTime)
            DeleteScreenShot("health")
    except Exception:
        print("Health error")
        exit()

def OhShitGiveMeMana():
    pythoncom.CoInitialize()
    print("auto mana started")
    try:
        while True:
            if not active:
                continue
            time.sleep(0.6)
            MakeScreenShot("mana")
            if GetPixelColor("mana") != (19, 80, 160):
                PressKey("é")
                DeleteScreenShot("mana")
                time.sleep(manaPotionTime)
            DeleteScreenShot("mana")
    except Exception:
        print("Mana error")
        exit()

def statusChecker(queue):
    print("status checker started")
    global active
    global healthPotionTime
    global manaPotionTime
    message = ""
    while True:
        try:
            if queue.empty():
                continue
            message = queue.get()
            if type(message) == bool:
                active = message
                continue
            elif message[0] == "H":
                healthPotionTime = float(message.strip("H"))
                print(healthPotionTime)
                print(type(healthPotionTime))
                continue
            elif message[0] == "M":
                manaPotionTime = float(message.strip("M"))
                print(manaPotionTime)
                print(type(manaPotionTime))
                continue
        except Exception:
            print("status checker error")
            exit()


def PoEActive():
    if "PathOfExileSteam.exe" not in (p.name() for p in psutil.process_iter(attrs=['name'])):
        exit("PoE is not running")


if __name__ == '__main__':

    PoEActive()
    DeleteScreenShot("health")
    DeleteScreenShot("mana")

    queue = queue.Queue()
    gui = threading.Thread(target=interface, args=(queue,))
    gui.start()
    status = threading.Thread(target=statusChecker, args=(queue,))
    status.start()
    autoHealth = threading.Thread(target=OhShitGiveMeHealth)
    autoHealth.start()
    autoMana = threading.Thread(target=OhShitGiveMeMana)
    autoMana.start()





