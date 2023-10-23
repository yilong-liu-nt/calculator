from tkinter import *
from tkinter import filedialog
from functools import partial
import numpy as np

from PIL import Image, ImageTk

img1 = None
img2 = None
resultImage = None
image_size = (256, 256)

def upload_image_1(gui):
    global img1

    file_types = [('Png Files', '*.Png'), ('Jpg Files', '*.Jpg')]
    filename = filedialog.askopenfilename(filetypes=file_types)

    img1 = Image.open(filename)
    resized_image = img1.resize(image_size)
    img1= ImageTk.PhotoImage(resized_image)

    Label(gui, image=img1).grid(row=3, column=0)


def upload_image_2(gui):
    global img2

    file_types = [('Png Files', '*.Png'), ('Jpg Files', '*.Jpg')]
    filename = filedialog.askopenfilename(filetypes=file_types)
    
    img2 = Image.open(filename)
    resized_image = img2.resize(image_size)
    img2= ImageTk.PhotoImage(resized_image)

    Label(gui, image=img2).grid(row=3, column=1)


def image_add(gui):
    global img1
    global img2
    global resultImage

    img1_arr = np.asarray(ImageTk.getimage(img1))
    img1_arr = np.asarray(ImageTk.getimage(img2))

    addition = (img1_arr + img1_arr)//2

    resultImage = ImageTk.PhotoImage(Image.fromarray(addition))

    Label(gui, image=resultImage).grid(row=3, column=2)



def image_minus(gui):
    global img1
    global img2
    global resultImage

    img1_arr = np.asarray(ImageTk.getimage(img1))
    img1_arr = np.asarray(ImageTk.getimage(img2))

    addition = (img1_arr - img1_arr)//2

    resultImage = ImageTk.PhotoImage(Image.fromarray(addition))

    Label(gui, image=resultImage).grid(row=3, column=2)


def imageWindow(master):
    gui = Toplevel(master)

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Image Calculator")

    # set the configuration of GUI window
    gui.geometry("540x800")
    
    
    button_plus = Button(gui, text='-', command=partial(image_minus, gui)).grid(row=0, column=0)
    button_minus = Button(gui, text='+', command=partial(image_add, gui)).grid(row=0, column=1)
    remove_color_r = Button(gui, text='Remove R').grid(row=1, column=0)
    remove_color_g = Button(gui, text='Remove G').grid(row=1, column=1)
    remove_color_b = Button(gui, text='Remove B').grid(row=1, column=2)
    
    
    upload_button_1 = Button(gui, text='Upload Image 1',
                           command=partial(upload_image_1, gui)).grid(row=2, column=0)
    
    upload_button_2 = Button(gui, text='Upload Image 2',
                           command=partial(upload_image_2, gui)).grid(row=2, column=1)
    

    arr=np.ones(image_size)
    img=Image.fromarray(arr)
    img1=ImageTk.PhotoImage(img)

    arr=np.zeros(image_size)
    img=Image.fromarray(arr)
    img2=ImageTk.PhotoImage(img)


    Label(gui, image=img1).grid(row=3, column=0)
    Label(gui, image=img2).grid(row=3, column=1)
