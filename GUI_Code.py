from Tkinter import*

#############################################################################################################################################################
#functions for heater and thermometer



def start_and_end_temp_control():
          #used to turn on/off temperature control
          pass

def turnOn():
          #turns the Heater on
          pass

def turnOff():
          #turns the heater off
          pass

def readArduino():
          #reads Arduino
          pass

def findTemp():
          #uses analog val from Arduino to
          #calculate the temperature
          analogVal = 0 #this value is taken from the arduino Serial monitor
          finalTemp = 0  #replace "0" with the calibration equation ex.  finalTemp = analogVal*4+225
          #return finalTemp

def Decide_on_or_off(temperature, wantedTemp):
          if (temp > wantedTemp+5):
                    turnOff()
          elif(temp < wantedTemp-5):
                    turnOn()

#############################################################################################################################################################
#GUI
class Application(Frame):
          def __init__(self,master):
                    Frame.__init__(self,master)
                    self.button1 = Button(master, fg = "red")# command = self.start_and_end_temp_control())
                    self.button2 = Button(master, fg = "red")# command = increase_set_temp())
                    self.button3 = Button(master, fg = "red")# command = decrease_set_temp())
                              




WIDTH = 1080
Height = 1920

window = Tk()
App = Application(window)
window.mainloop()




