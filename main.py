# import everything from tkinter module
from tkinter import *
from functools import partial
from basic import basicWindow
from text import textWindow
from image import imageWindow


if __name__ == "__main__":

    master = Tk()
    master.title("Calculator Home Screen")
    master.geometry("1000x600")

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
            ).grid(row=1, column=1)
    
    btn3 = Button(master,
            text="Text",
            height= 5, width = 20,
            command=partial(textWindow, master)
            ).grid(row=1, column=2,)
    
    instruction_text = """
        1.You may click any one of the three buttons above, Basic, Image, or Text
        2.Basic mode is self-explanitory, it is quite literally the basic calculator
        3.Image mode is more sophisticated, you can set the RGB, these three numbers must be from 0-255
        4.If R, G, and B are all zero, you will have no image, so click + to reset it(only if you have another image)
        5.You may find the edges of the images in the image, just click <Edge detection> a few times
        6.Blur the image! Be free and do what you want. The image calculator will allow JPG and PNG files
        7.Text mode is not much, so if you feel lonely while in text mode, just kill it.
        8.Thats it!
    """
    instructions = Label(master, text=instruction_text).grid(row=2, columnspan=4, column=0)

    # start the GUI
    master.mainloop()


