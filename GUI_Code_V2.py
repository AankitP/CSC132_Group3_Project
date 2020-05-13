from tkinter import *

from math import *
# import RPi.GPIO as GPIO
import time

# import serial

#############################################################################################################################################################
# functions for heater and thermometer

Relay = 17


# GPIO.setup(Relay, GPIO.OUT)

def turnOn():
    # send voltage out GPIO pin ___ to trigger relay
    #          GPIO.output(Relay, True)
    App.relay_Status = "on"
    pass


def turnOff():
    # cuts voltage to GPIO pin ____ to untrigger relay
    #          GPIO.output(Relay, False)
    App.relay_Status = "off"
    pass


def readArduino():
    # reads Arduino
    # port is the serial port that the serial monitor is read from, this may be different
    # in your system, to find, open serial monitor from the arduino IDE
    # look at the tab in the taskbar, and the name of that is what you put instead of ACM0
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    counter = 0
    return int(ser.readline())


def findTemp():
    # uses analog val from Arduino to
    # calculate the temperature
    analogVal = readArduino()  # this value is taken from the arduino Serial monitor
    Temp = 15.108 * math.exp(0.0032 * AnalogVal)  # convert the analog value to temperature value
    # return temperature
    App.temp = Temp
    return Temp

def Button_press():
    if(App.Button_Color == "Green"):
        App.Button_Color = "red"
    else:
        App.Button_Color = "Green"


def Decide_on_or_off(temp, wantedTemp):
    if (temp >= wantedTemp):
        turnOff()
    elif (temp < wantedTemp - 5):
        turnOn()



##########################################################################################

#Use this to change the font to whatever you like
font_ = 'Comic Sans MS'

##########################################################################################
# GUI
class App(Frame):
    def __init__(self, master, Button_Color, status, relay_Status, temp_Status, temp):
        self.Button_Color = 'Red'
        self.status = "idle"
        self.relay_Status = "off"
        self.temp_Status = "not set"
        self.temp = 75


        Frame.__init__(self, master)

        #used for plcing the actual temp text and switch text
        self.Label0 = Label(master, text="\n", font=(font_, 5, 'bold italic'))
        self.Label0.grid(row=2, column=1)

        self.Label1 = Label(master, text=" Actual Temperature", font=(font_, 30, 'bold italic'))
        self.Label1.grid(row=3, column=1)

        self.Label2 = Label(master, text="75", font=(font_, 40, 'bold italic'))
        self.Label2.grid(row=4, column=1)

        self.Label3 = Label(master, text="Status - {}".format(self.status), font=(font_, 20, 'bold italic'))
        self.Label3.grid(row=6, column=1)

        #used for seperating the Actual temp and master switch text
        self.Label3_5 = Label(master, text="\n\n ", font=(font_, 10, 'bold italic'))
        self.Label3_5.grid(row=7, column=1)

        self.Label4 = Label(master, text="Master Switch", font=(font_, 20, 'bold italic'))
        self.Label4.grid(row=8, column=1)

        self.Label5 = Label(master, text="Tap to activate", font=(font_, 20, 'bold italic'))
        self.Label5.grid(row=9, column=1)

        self.Label6 = Label(master, text="Green - On", font=(font_, 20, 'bold italic'))
        self.Label6.grid(row=10, column=1)

        self.Label7 = Label(master, text="Red - Off", font=(font_, 20, 'bold italic'))
        self.Label7.grid(row=11, column=1)

        self.Master_Switch = Button(master, text='', background=self.Button_Color, command = Button_press())  # Green: #00FF00      Red: #ff0000
        self.Master_Switch.grid(row=9, column=2, rowspan=6, columnspan=2, sticky=N + S + W + E)

        #used to format the set temp into the correct position
        self.Label7_5 = Label(master, text="\t", font=(font_, 15, 'bold italic'))
        self.Label7_5.grid(row=3, column=2)


        self.Label8 = Label(master, text="Set Temp", font=(font_, 30, 'bold italic'))
        self.Label8.grid(row=3, column=5)

        #put a variable where 100 is so that you can change it by pressing the buttons
        self.Label9 = Label(master, text=self.temp, font=(font_, 30, 'bold italic'))
        self.Label9.grid(row=4, column=5)

        #used for seperating the set temp and statuses
        #self.Label9_5 = Label(master, text="\n\n ", font=(font_, 20, 'bold italic'))
        #self.Label9_5.grid(row=5, column=4)

        #put a .format in the text portion with a variable to change the status
        self.Label10 = Label(master, text="Relay status - {}".format(self.relay_Status), font=(font_, 10, 'bold italic'))
        self.Label10.grid(row=8, column=5)

        self.Label11 = Label(master, text="Temp status - {}".format(self.temp_Status), font=(font_, 10, 'bold italic'))
        self.Label11.grid(row=10, column=5)

    # def initUI(self):
    #     self.master.title("Lines")
    #     self.pack(fill=BOTH, expand=1)
    #
    #     canvas = Canvas(self)
    #     canvas.create_rectangle(533, 240, 533, -240, outline = "000000", fill = "000000", width = 1)
    #     canvas.create_line(300, 35, 300, 200, dash=(4, 2))
    #     canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    #
    #     canvas.pack(fill=BOTH, expand=1)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def Button_Color(self):
        return self._Button_Color

    @Button_Color.setter
    def Button_Color(self, value):
        self._Button_Color = value

    @property
    def relay_Status(self):
        return self._relay_Status

    @relay_Status.setter
    def relay_Status(self, value):
        self._relay_Status = value

    @property
    def temp_Status(self):
        return self._temp_Status

    @temp_Status.setter
    def temp_Status(self, value):
        self._temp_Status = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value


    def say(self):
        print("something")

    #def get_Status(self):
    #    return self.status_
    #def set_Status(self):
    #    self.status_ = "off"
    #    return self.status_



WIDTH = 800
HEIGHT = 800

window = Tk()
window.geometry("800x480")
app = App(window, 'Green', 'idle', 'off', 'not set',0)

window.mainloop()
