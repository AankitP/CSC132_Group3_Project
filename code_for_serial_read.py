import time
import serial

#this is the code used to read serial monitor

def readArduino():
	#reads Arduino
	ser = serial.Serial(
		port = '/dev/ttyACM0',
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	   )

	counter = 0
	return ser.readline()

a = readArduino()
print (a)