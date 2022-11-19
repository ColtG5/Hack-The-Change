import tkinter as tk
import time

first_text = "Hello There!"
light_blue = "#00DEFF"
background_image = tk.PhotoImage(file="xp-hills.jpg")

def displayScreenOne(window):
    
    main_frame = tk.Frame(window, bg=light_blue, height=1080, width=1920)
    main_frame.pack(fill="both", expand="true")
    window.geometry("1920x1080")

    label_image = tk.Label(window, i=background_image)
    label_image.pack()

    # first_text = tk.Label(root, text=first_text, font="")
