from time import sleep     
import os
from pynput.keyboard import Key, Controller
import data_handler.arduino as arduino
import pdf.pdf_config as pdf_config

def start_pdf_reader(path):
    os.system(pdf_config.PDF_APP + ' ' + path)
    keyboard = Controller()

    while True:
        data = arduino.get_data()

        if (data == 'M1'):
            keyboard.press(Key.shift_l)
            keyboard.press(Key.space)
            sleep(0.1)
            keyboard.release(Key.shift_l)
            keyboard.release(Key.space)
        elif (data == 'M2'):
            keyboard.press(Key.space)
            sleep(0.1)
            keyboard.release(Key.space)
