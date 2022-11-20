import tkinter as tk
from PIL import ImageTk, Image
import time

first_text = "Hello There!"
light_blue = "#00DEFF"

def displayWindowOne():
    window = tk.Tk()
    window.geometry("1920x1080")
    window.resizable(0,0)
    
    main_frame = tk.Frame(window, height=1080, width=1920, bg="black")
    main_frame.pack(fill="both", expand="true")
    # main_frame.pack(side=tk.TOP)
    # main_frame.place(anchor='center', relx=0.5, rely=0.5)
    print("making image")
    bg_image = ImageTk.PhotoImage(Image.open("xp-hills.png"))
    background = tk.Label(main_frame, i=bg_image)
    # print("displaying image")
    background.pack()
    # print("boutta sleep")
    # print("woke up")

    # second_frame = tk.Frame(window, height=1080, width=1920, bg="black")
    # second_frame.pack(fill="both", expand="true")

    # bg_image = ImageTk.PhotoImage(Image.open("man-waving.png"))
    # background = tk.Label(main_frame, i=bg_image)
    # background.pack()

    time.sleep(1)
    print("aftersleep")
    print("after withdraw")
    window.quit()


def displayWindowTwo():
    window = tk.Tk()
    window.geometry("1920x1080")
    window.resizable(0,0)
    
    main_frame = tk.Frame(window, height=1080, width=1920, bg="black")
    main_frame.pack(fill="both", expand="true")
    # main_frame.pack(side=tk.TOP)
    # main_frame.place(anchor='center', relx=0.5, rely=0.5)

    bg_image = ImageTk.PhotoImage(Image.open("man-waving.png"))
    background = tk.Label(main_frame, i=bg_image)
    background.pack()

    window.mainloop()
    time.sleep(1.5)
    window.withdraw()