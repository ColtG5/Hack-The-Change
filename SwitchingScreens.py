import tkinter as tk
from PIL import ImageTk, Image
import time
import ElevatorReduction

TIMING_INTRO = 3
TIMING_PIC1 = 8.5
TIMING_PIC2 = 9

def displayAndSwitchWindows(window):

    window.geometry("1920x1080")
    window.resizable(0,0)
    window.attributes("-fullscreen", True)
    print(window)
    window.bind("<KeyPress>", lambda event, w=window: keyPressed(event, w))
    
    main_frame = tk.Frame(window, height=1080, width=1920, bg="black")
    main_frame.pack(fill="both", expand="true")
    window.update()

    while True:

        print("checking for motion")
        ElevatorReduction.sensor()

        intro_image = ImageTk.PhotoImage(Image.open("1.png"))
        intro = tk.Label(main_frame, i=intro_image)

        bg_image1 = ImageTk.PhotoImage(Image.open("2.png"))
        background1 = tk.Label(main_frame, i=bg_image1)

        bg_image2 = ImageTk.PhotoImage(Image.open("3.png"))
        background2 = tk.Label(main_frame, i=bg_image2)

        intro.pack()
        background1.pack()
        background2.pack()
        window.update()

        time.sleep(TIMING_INTRO)

        intro.destroy()
        window.update()

        time.sleep(TIMING_PIC1)

        background1.destroy()
        window.update()

        time.sleep(TIMING_PIC2)

        background2.destroy()
        window.update()

def keyPressed(event, window):

    window.destroy()
    window.update()