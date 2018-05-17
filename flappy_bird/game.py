from pynput.keyboard import Key, Controller
import data_handler.arduino as arduino
from time import sleep     
import os

def start_game(path):
    os.startfile(path)
    keyboard = Controller()

    while True:
        data = arduino.get_data()

        if (data == 'M1'):
            keyboard.press(Key.ctrl_l)
            keyboard.press(Key.enter)

            keyboard.release(Key.ctrl_l)
            keyboard.release(Key.enter)
        elif (data == 'M2'):
            keyboard.press(Key.space)
            sleep(0.1)
            keyboard.release(Key.space)
