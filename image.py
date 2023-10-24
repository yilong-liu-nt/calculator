from tkinter import *
from tkinter import filedialog
from functools import partial
import numpy as np

from PIL import Image, ImageTk, ImageFilter

# https://realpython.com/image-processing-with-the-python-pillow-library/#:~:text=PIL%20stands%20for%20Python%20Imaging,includes%20support%20for%20Python%203.

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
    img2_arr = np.asarray(ImageTk.getimage(img2))

    addition = img1_arr//2 + img2_arr//2

    resultImage = ImageTk.PhotoImage(Image.fromarray(addition))

    Label(gui, image=resultImage).grid(row=3, column=2)



def image_minus(gui):
    global img1
    global img2
    global resultImage

    img1_arr = np.asarray(ImageTk.getimage(img1))
    img2_arr = np.asarray(ImageTk.getimage(img2))

    minus_arr = img1_arr - img2_arr

    resultImage = ImageTk.PhotoImage(Image.fromarray(minus_arr))

    Label(gui, image=resultImage).grid(row=3, column=2)


def image_transpose(gui):
    """
    Rotate 45 degree
    """
    global resultImage

    my_image = ImageTk.getimage(resultImage)
    rotated_image = my_image.rotate(45)
    resultImage = ImageTk.PhotoImage(rotated_image)

    Label(gui, image=resultImage).grid(row=3, column=2)


def blur_image(gui):
    global resultImage

    my_image = ImageTk.getimage(resultImage)
    blurred_image = my_image.filter(ImageFilter.BLUR)
    resultImage = ImageTk.PhotoImage(blurred_image)

    Label(gui, image=resultImage).grid(row=3, column=2)


def edge_image(gui):
    global resultImage


    my_image = ImageTk.getimage(resultImage)
    edge_restored_image = my_image.filter(ImageFilter.EDGE_ENHANCE)
    resultImage = ImageTk.PhotoImage(edge_restored_image)

    Label(gui, image=resultImage).grid(row=3, column=2)

def imageWindow(master):
    global img1
    global img2
    global resultImage
    
    gui = Toplevel(master)

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Image Calculator")

    # set the configuration of GUI window
    gui.geometry("900x800")
    
    
    button_plus = Button(gui, text='-', command=partial(image_minus, gui)).grid(row=0, column=0)
    button_minus = Button(gui, text='+', command=partial(image_add, gui)).grid(row=0, column=1)
    button_minus = Button(gui, text='Transpose', command=partial(image_transpose, gui)).grid(row=4, column=0)

    remove_color_r = Button(gui, text='Remove R').grid(row=1, column=0)
    remove_color_g = Button(gui, text='Remove G').grid(row=1, column=1)
    remove_color_b = Button(gui, text='Remove B').grid(row=1, column=2)
    
    
    upload_button_1 = Button(gui, text='Upload Image 1',
                           command=partial(upload_image_1, gui)).grid(row=2, column=0)
    
    upload_button_2 = Button(gui, text='Upload Image 2',
                           command=partial(upload_image_2, gui)).grid(row=2, column=1)
    
    blur_button= Button(gui, text='Blur Image',
                           command=partial(blur_image, gui)).grid(row=4, column=1)
    edge_button= Button(gui, text='Edge Detection',
                           command=partial(edge_image, gui)).grid(row=4, column=2)
    
    
    Label(gui, text = "Result").grid(row=2, column=2)

    img=Image.new("RGB", image_size, (255, 255, 255))
    img1=ImageTk.PhotoImage(img)
    Label(gui, image=img1).grid(row=3, column=0)

    arr = np.zeros((image_size[0], image_size[1], 4), dtype= int)
    img2=ImageTk.PhotoImage(Image.fromarray(arr, mode="RGB"))
    Label(gui, image=img2).grid(row=3, column=1)


    result = Image.new("RGB", image_size, (0, 0, 0))
    resultImage = ImageTk.PhotoImage(result)
    Label(gui, image=resultImage).grid(row=3, column=2)
