from Tkinter import*

class turnOn():
          #turns the Heater on

class turnOff():
          #turns the heater off

class readArduino():
          #reads Arduino

class findTemp():
          #uses analog val from Arduino to
          #calculate the temperature
          analogVal = 0 #this value is taken from the arduino Serial monitor
          finalTemp = 0  #replace "0" with the calibration equation ex.  finalTemp = analogVal*4+225
          return finalTemp

class Decide(temp, wantedTemp):
          if (temp > wantedTemp+5):
                    turnOff()
          elif(temp < wantedTemp-5):
                    turnOn()


          
