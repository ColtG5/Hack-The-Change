import tkinter as tk                
from tkinter import font as tkfont 
from PIL import ImageTk, Image
import time

class ElevatorReductionWindows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, height=1080, width=1000)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstWindow, SecondWindow, ThirdWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FirstWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class FirstWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1000, height=1000)
        self.controller = controller
        # label = tk.Label(self, text="This is the first page", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        # bg_image = ImageTk.PhotoImage(Image.open("/home/pi/Documents/Coding Projects/Hack-The-Change/xp-hills.png"))

        # background = tk.Label(self, i=bg_image)
        # background.pack(side="top", fill="x", pady=0)

        button = tk.Button(self, text="Go to the second page",
                            command=lambda: controller.show_frame("SecondWindow"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        button.pack()
        # button2.pack()


class SecondWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the second page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the third page",
                           command=lambda: controller.show_frame("ThirdWindow"))
        button.pack()


class ThirdWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the third page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()


# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()