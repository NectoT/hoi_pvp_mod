from pynput.keyboard import Key
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as ButtonListener
from PIL import ImageGrab
from time import sleep
from threading import Lock
import pandas

path = "C:/Users/nectot/Documents/Paradox Interactive/Hearts of Iron IV/mod/pvp/map/definition.csv"
coast_on_click = True

definition = pandas.read_csv(
    path, names=['r', 'g', 'b', 'land_type', 'is_coast', 'terrain', 'continent']
)

cursor_pos = (0, 0)

lock = Lock()

def modify_coast(color, is_coast):
    for i in range(1, definition.shape[0]):
        if definition['r'][i] == color[0] and definition['g'][i] == color[1] and definition['b'][i] == color[2]:
            print("Province update written")
            coast_str = 'true' if is_coast else 'false'
            definition.loc[i, 'is_coast'] = coast_str
            return

def save_definition():
    definition.to_csv(path, header=False, index=True)
    print("definition updated")

def on_release(key):
    global coast_on_click
    if key == Key.end:
        save_definition()

    if key == Key.caps_lock:
        coast_on_click = not coast_on_click

    if key != Key.shift_l:
        return True

    snapshot = ImageGrab.grab()
    with lock:
        pixel = snapshot.getpixel(cursor_pos)
    modify_coast(pixel, coast_on_click)
    print(pixel)

    return True

def on_move(x, y):
    global cursor_pos
    with lock:
        cursor_pos = (x, y)

button_listener = ButtonListener(on_move=on_move)
button_listener.start()
keyboard_listener = KeyboardListener(on_release=on_release)
keyboard_listener.start()

while keyboard_listener.is_alive():
    sleep(1)

print("Coast selecting finished")