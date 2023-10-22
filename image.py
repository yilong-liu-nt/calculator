from tkinter import *
from tkinter import filedialog
from functools import partial

from PIL import Image, ImageTk

img = None

def upload_image(gui):
    global img

    file_types = [('Png Files', '*.Png'), ('Jpg Files', '*.Jpg')]
    filename = filedialog.askopenfilename(filetypes=file_types)
    img = ImageTk.PhotoImage(file=filename)
    print(filename)
    if img is not None:
        print("Here is image")
    # b1 = Button(gui, text="Upload Image", image=img)

    Label(gui, image=img).grid(row=1, column=0)


def imageWindow(master):
    global img
    gui = Toplevel(master)

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Image Calculator")

    # set the configuration of GUI window
    gui.geometry("540x300")

    upload_button = Button(gui, text='Upload Image',
                           command=partial(upload_image, gui)).grid(row=0, column=0)
    