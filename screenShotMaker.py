from PIL import ImageGrab
import os


def MakeScreenShot(ressource):
    if ressource == "mana":
        filePath = "M:/coding/autoMana/screenshot/screen.jpg"
        screenshot = ImageGrab.grab(bbox=(1797, 993, 1798, 994))
    else:
        filePath = "M:/coding/autoMana/screenshot/screen2.jpg"
        screenshot = ImageGrab.grab(bbox=(110, 1010, 111, 1011))

    screenshot.save(filePath)


def DeleteScreenShot(ressource):
    if ressource == "mana":
        filePath = "M:/coding/autoMana/screenshot/screen.jpg"
    else:
        filePath = "M:/coding/autoMana/screenshot/screen2.jpg"
    try:
        os.remove(filePath)
    except FileNotFoundError:
        pass
