import tkinter.font
import RPi.GPIO
from tkinter import *
from gpiozero import LED

# Set the GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Define LED objects for Red, Green, and White LEDs
Red = LED(5)
Green = LED(13)
White = LED(26)

# Create the main window
win = Tk()
win.title("LED BLINK")
myFont = tkinter.font.Font(family='Times New Roman', size=14, weight="bold")

# Function to control the Red LED
def REDON():
    if Red.is_lit:
        Red.off()
        redButton["text"] = "TURN ON RED LED"
    else:
        Red.on()
        redButton["text"] = "TURN OFF RED LED"

# Function to control the Green LED
def GREENON():
    if Green.is_lit:
        Green.off()
        greenButton["text"] = "TURN ON GREEN LED"
    else:
        Green.on()
        greenButton["text"] = "TURN OFF GREEN LED"

# Function to control the White LED
def WHITEON():
    if White.is_lit:
        White.off()
        whiteButton["text"] = "TURN ON WHITE LED"
    else:
        White.on()
        whiteButton["text"] = "TURN OFF WHITE LED"

# Function to clean up GPIO and close the window
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create buttons for LED control
redButton = Button(win, text="TURN ON RED LED", font=myFont, command=REDON)
redButton.grid(row=0, column=1)

greenButton = Button(win, text="TURN ON GREEN LED", font=myFont, command=GREENON)
greenButton.grid(row=0, column=2)

whiteButton = Button(win, text="TURN ON WHITE LED", font=myFont, command=WHITEON)
whiteButton.grid(row=0, column=3)

exitButton = Button(win, text="EXIT WINDOW", font=myFont, command=close, bg='red')
exitButton.grid(row=2, column=2)

# Set up a protocol for handling window close event
win.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter main event loop
win.mainloop()
