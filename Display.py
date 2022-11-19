import tkinter as tk
from PIL import ImageTk, Image
import time

first_text = "Hello There!"
light_blue = "#00DEFF"

def displayTheScreen():
    window = tk.Tk()
    
    # main_frame = tk.Frame(window, bg=light_blue, height=1080, width=1920)
    # main_frame.pack(fill="both", expand="true")
    # window.geometry("1920x1080")

    print("")
    background_image = ImageTk.PhotoImage(Image.open("/home/pi/Documents/Coding Projects/Hack-The-Change/xp-hills.png"))

    label_image = tk.Label(window, i=background_image)
    label_image.pack()

    # first_text = tk.Label(root, text=first_text, font="")

    window.mainloop()