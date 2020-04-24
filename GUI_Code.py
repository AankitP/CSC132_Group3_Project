from Tkinter import*
from math import*
import RPi.GPIO as GPIO
import time
import serial

#############################################################################################################################################################
#functions for heater and thermometer

Relay = 17
GPIO.setup(Relay, GPIO.OUT)

def turnOn():
          #send voltage out GPIO pin ___ to trigger relay
          GPIO.output(Relay, True)
          pass

def turnOff():
          #cuts voltage to GPIO pin ____ to untrigger relay
          GPIO.output(Relay, False)
          pass

def readArduino():
#reads Arduino
          #port is the serial port that the serial monitor is read from, this may be different
          #in your system, to find, open serial monitor from the arduino IDE
          #look at the tab in the taskbar, and the name of that is what you put instead of ACM0
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

def findTemp():
          #uses analog val from Arduino to
          #calculate the temperature
          analogVal = readArduino() #this value is taken from the arduino Serial monitor
          Temp = 15.108 * math.exp(0.0032*AnalogVal)   #convert the analog value to temperature value
          #return temperature
          return Temp
          

def Decide_on_or_off(temp, wantedTemp):
          if (temp >= wantedTemp):
                    turnOff()
          elif(temp < wantedTemp-5):
                    turnOn()

#main loop
while(true):
          actual_Temp = findTemp()
          i = 0
          if (i == 0):
                    wantedTemp = raw_input("What temperature do you want your coffee to be set at?")
                    i++
         Decide_on_or_off(actual_Temp, wantedTemp)
         
                    
          


#############################################################################################################################################################
#GUI
class Application(Frame):
          def __init__(self,master):
                    Frame.__init__(self,master)
                    self.button1 = Button(master, fg = "red")# command = self.start_and_end_temp_control())
                    self.button2 = Button(master, fg = "red")# command = increase_set_temp())
                    self.button3 = Button(master, fg = "red")# command = decrease_set_temp())
                              

################################################################################


WIDTH = 1080
Height = 1920

window = Tk()
App = Application(window)
window.mainloop()




