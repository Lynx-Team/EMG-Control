import serial
from time import sleep
from . import arduino_config as config

arduino = serial.Serial(config.PORT_ID, baudrate=config.BAUDRATE, timeout=config.TIMEOUT)

def get_string():
    return arduino.readline().rstrip()

def get_data():
    return str(get_string()).replace('\'', '').replace('b', '') 
