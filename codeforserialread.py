import RPi.GPIO as GPIO
import math
import time
from time import sleep
import serial
warmer = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(warmer, GPIO.OUT)
GPIO.output(warmer, GPIO.LOW)
#chart for temps
print "Here is a basic temp chart, enter the vlaue on the left side to set the desired temperature"
print
print "70F  = 470"
print "80F  = 510"
print "90F  = 570"
print "100F = 610"
print "110F = 640"
print "120F = 670"
print "130F = 690"
print "140F = 720"
print "150F = 740"
print "160F = 750"
print "170F = 760"
print "180F = 770"
print "190F = 780"
print "200F = 790"

x = input("What temperature would you like?: ")
temp = 312.17 * math.log(x) - 838.49
print temp



#this is the code used to read serial monitor

def readArduino(temp):
        #reads Arduino
        if __name__ == '__main__':
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
                ser.flush()

                while True:
                        if ser.in_waiting > 0:
                                while True:
                                        ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
                                        ser.flush()
                                        line = ser.read(5).strip()
                                        line1 = int(float(line))
                                        print "this is line1==={}".format(line1)
                                        if (line1 < temp):
                                                print "Warming! current temp= {}".format(line1)
                                                print "Warming! set temp    = {}".format(temp)
                                                GPIO.output(warmer, GPIO.HIGH)
                                                sleep(1)
                                        elif (line1 > temp):
                                                print "Cooling! current temp= {}".format(line1)
                                                print "Cooling! set temp    = {}".format(temp)
                                                GPIO.output(warmer, GPIO.LOW)
                                                sleep(1)



temp = readArduino(temp)
GPIO.cleanup()
