import tkinter as tk
from PIL import ImageTk, Image
import time

class FrameSwitcher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(FirstWindow)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class FirstWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the first page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(SecondWindow)).pack()
        # tk.Button(self, text="Open page two",
        #           command=lambda: master.switch_frame(PageTwo)).pack()

class SecondWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the second page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(ThirdWindow)).pack()

class ThirdWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # tk.Label(self, text="This is the third page").pack(side="top", fill="x", pady=10)
        # tk.Button(self, text="Return to start page",
        #           command=lambda: master.switch_frame(StartPage)).pack()