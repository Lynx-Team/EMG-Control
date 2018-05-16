import serial
from time import sleep

port_id = 'COM4'
arduino = serial.Serial(port_id, baudrate=9600, timeout=0)

while True:
    data = arduino.readline().rstrip()
    print(data)
    
    sleep(0.3)
