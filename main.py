import tkinter as tk
import time
import ElevatorReduction


def checkForMotion():
    print("checking for motion")
    ElevatorReduction.main()
    return True

def onWake():
    print("sensor detected motion! Wake the screen!")

def displayTheScreen():
    root = tk.Tk()



    root.mainloop()

def main():

    # Continous loop to wait for motion to be detected
    checkForMotion()
    # Once we have motion, go into initial procedure to wake up the screen
    onWake()

    #Create the UI to display for the user
    displayTheScreen()
    

if __name__ == '__main__':
    main()