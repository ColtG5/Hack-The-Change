import tkinter as tk
from PIL import ImageTk, Image
import time

first_text = "Hello There!"
light_blue = "#00DEFF"

def displayWindows():
    window = tk.Tk()
    window.geometry("1920x1080")
    window.resizable(0,0)
    
    main_frame = tk.Frame(window, height=1080, width=1920, bg="black")
    main_frame.pack(fill="both", expand="true")
    # main_frame.pack(side=tk.TOP)
    # main_frame.place(anchor='center', relx=0.5, rely=0.5)
    print("making images")

    intro_image = ImageTk.PhotoImage(Image.open("xp-hills.png"))
    intro = tk.Label(main_frame, i=intro_image)

    bg_image1 = ImageTk.PhotoImage(Image.open("ABLE TO TAKE THE STAIRS (3).png"))
    background1 = tk.Label(main_frame, i=bg_image1)

    bg_image2 = ImageTk.PhotoImage(Image.open("Able to take the stairs (4).png"))
    background2 = tk.Label(main_frame, i=bg_image2)

    intro.pack()
    background1.pack()
    background2.pack()
    window.update()

    time.sleep(1.2)

    intro.destroy()
    window.update()

    time.sleep(3.5)

    background1.destroy()
    window.update()

    time.sleep(3)

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