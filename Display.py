import tkinter as tk
import time

first_text = "Hello There!"
light_blue = "00DEFF"

def displayTheScreen():
    root = tk.Tk()
    
    main_frame = tk.Frame(root, bg="black", height=1080, width=1920)
    main_frame.pack(fill="both", expand="true")

    root.geometry("1920x1080")

    # first_text = tk.Label(root, text=first_text, font="")

    root.mainloop()