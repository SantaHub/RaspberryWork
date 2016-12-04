import serial
import RPi.GPIO
import time
scr = serial.Serial('/dev/ttyACM1',9600)

while 1:
	time.sleep(1)
	scr.write('A')
