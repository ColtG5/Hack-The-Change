import tkinter as tk
import time
import ElevatorReduction
from ElevatorReductionWindows import *
from Screens import *

def checkForMotion():
    ElevatorReduction.sensor()
    return

def onWake():
    print("sensor detected motion! Wake the screen!")

def displayScreens():

    # displayTheScreens()

    elevator_reduction = ElevatorReductionWindows()
    elevator_reduction.mainloop()
    

def main():

    # Continous loop to wait for motion to be detected
    print("checking for motion")
    checkForMotion()
    # Once we have motion, go into initial procedure to wake up the screen
    onWake()

    #Create the UI to display for the user

    displayScreens()

    # displayWindowOne()

    # displayWindowTwo()
    

if __name__ == '__main__':
    main()