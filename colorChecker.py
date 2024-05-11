from PIL import Image

def GetPixelColor(ressource):
    if ressource == "mana":
        im = Image.open("M:/coding/autoMana/screenshot/screen.jpg")
    else:
        im = Image.open("M:/coding/autoMana/screenshot/screen2.jpg")

    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((0, 0))

    return r, g, b