# import everything from tkinter module
from tkinter import *
from functools import partial
from basic import basicWindow
from text import textWindow
from image import imageWindow


if __name__ == "__main__":

    master = Tk()
    master.title("Calculator Home Screen")
    master.geometry("500x600")

    label = Label(master, text= "Welcome to use the following calculators.").grid(row=0, column=0, columnspan=2)


    # a button widget which will open a
    # new window on button click
    btn = Button(master,
            text="Basic",
            height= 5, width = 20,
            command=partial(basicWindow, master)
            ).grid(row=1, column=0)
    
    btn2 = Button(master,
            text="Image",
            height= 5, width = 20,
            command=partial(imageWindow, master)
            ).grid(row=2, column=0)
    
    btn3 = Button(master,
            text="Text",
            height= 5, width = 20,
            command=partial(textWindow, master)
            ).grid(row=3, column=0,)

    # start the GUI
    master.mainloop()


