from tkinter import *

from math import *
# import RPi.GPIO as GPIO
import time

# import serial

# Use this to change the font to whatever you like
##########################################################################################
#Variables
font_ = 'Comic Sans MS'
x = 1
status = 'idle'
temp = 75
current_temp = 0
relay_Status = "off"
temp_Status = "not set"
Relay = 17
#############################################################################################################################################################
# functions for heater and thermometer

# GPIO.setup(Relay, GPIO.OUT)

def turnOn():
    # send voltage out GPIO pin ___ to trigger relay
    #GPIO.output(Relay, True)
    pass


def turnOff():
    # cuts voltage to GPIO pin ____ to untrigger relay
    #GPIO.output(Relay, False)
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
    Label2['text'] = Temp
    return Temp


def Decide_on_or_off(temp, wantedTemp):
    if(Switch['bg'] == "Green"):
        if (temp >= wantedTemp):
            turnOff()
            Label10['text'] = "Relay status - off"
        elif (temp < wantedTemp - 5):
            turnOn()
            Label10['text'] = "Relay status - off"


##########################################################################################
# GUI
def button_color():
    global x
    global temp_Status
    if (x == 1):
        Switch['bg'] = 'Green'
        Label11['text'] = "temp status - set"
        # self.button = 'Green'
        x = x - 1
    else:
        Switch['bg'] = 'Red'
        Label11['text'] = "temp status - not set"
        # self.button = 'Red'
        x = x + 1

def increase_temp():
    global temp
    if (temp < 200):
        temp = temp + 5
        Label9['text'] = temp
    else:
        Label9['text'] = temp

def decrease_temp():
    global temp
    if (temp > 75):
        temp = temp - 5
        Label9['text'] = temp
    else:
        Label9['text'] = temp


Label0 = Label( text="\n", font=(font_, 5, 'bold italic'))
Label0.grid(row=2, column=1)

Label1 = Label( text="Actual Temperature", font=(font_, 30, 'bold italic'))
Label1.grid(row=3, column=1)

Label2 = Label( text="75", font=(font_, 40, 'bold italic'))
Label2.grid(row=4, column=1)

Label3 = Label( text="Status - {}".format(status), font=(font_, 20, 'bold italic'))
Label3.grid(row=6, column=1)

# used for seperating the Actual temp and switch text
Label3_5 = Label( text="\n\n ", font=(font_, 10, 'bold italic'))
Label3_5.grid(row=7, column=1)

Label4 = Label( text="Switch", font=(font_, 20, 'bold italic'))
Label4.grid(row=8, column=1)

Label5 = Label( text="Tap to activate", font=(font_, 20, 'bold italic'))
Label5.grid(row=9, column=1)

Label6 = Label( text="Green - On", font=(font_, 20, 'bold italic'))
Label6.grid(row=10, column=1)

Label7 = Label( text="Red - Off", font=(font_, 20, 'bold italic'))
Label7.grid(row=11, column=1)


Switch = Button( text='', borderwidth=0, highlightthickness=0, background='Red', command= button_color)  # Green: #00FF00      Red: #ff0000
Switch.grid(row=9, column=2, rowspan=7, columnspan=1, sticky=N + S + W + E )

# used to format the set temp into the correct position
Label7_5 = Label( text="\t", font=(font_, 15, 'bold italic'))
Label7_5.grid(row=3, column=2)

Label8 = Label( text="Set Temp", font=(font_, 30, 'bold italic'))
Label8.grid(row=3, column=5)

#buttons to adjust temperature value
Adjuster1 = Button(text='Decrease', borderwidth=0, highlightthickness=0, background='Red', activebackground = "blue", command = decrease_temp)
Adjuster1.grid(row = 4, column = 4)

Adjuster2 = Button(text='Increase', borderwidth=0, highlightthickness=0, background='Green', activebackground = "blue", command = increase_temp)
Adjuster2.grid(row = 4, column = 6)


# put a variable where 100 is so that you can change it by pressing the buttons
Label9 = Label( text=temp, font=(font_, 30, 'bold italic'))
Label9.grid(row=4, column=5)

# used for seperating the set temp and statuses
# Label9_5 = Label( text="\n\n ", font=(font_, 20, 'bold italic'))
# Label9_5.grid(row=5, column=4)

# put a .format in the text portion with a variable to change the status
Label10 = Label( text="Relay status - {}".format(relay_Status), font=(font_, 10, 'bold italic'))
Label10.grid(row=8, column=5)

Label11 = Label( text="Temp status - {}".format(temp_Status), font=(font_, 10, 'bold italic'))
Label11.grid(row=10, column=5)
mainloop()
