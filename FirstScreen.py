import tkinter as tk
from PIL import ImageTk, Image
import time

first_text = "Hello There!"
light_blue = "#00DEFF"

def displayScreenOne(window):
    
    # main_frame = tk.Frame(window, bg=light_blue, height=1080, width=1920)
    # main_frame.pack(fill="both", expand="true")
    # window.geometry("1920x1080")

    background_image = ImageTk.PhotoImage(Image.open("/home/pi/Documents/Coding Projects/Hack-The-Change/xp-hills.png"))

    bg_image = tk.Label(window, i=background_image)
    bg_image.pack()

    welcome_text = tk.Label(window, text="Hey You!", font="Courier", height=100, width=200, bg="black", fg="white")
    welcome_text.place(x=0, y=0)

    # first_text = tk.Label(root, text=first_text, font="")
