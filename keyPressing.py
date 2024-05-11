import win32com.client as comclt

def PressKey(key):

    wsh= comclt.Dispatch("WScript.Shell")
    wsh.AppActivate("Path Of Exile") # select another application
    try:
        wsh.SendKeys(key) # send the keys you want
    except Exception:
        print("Press error")
