import random
from tkinter import *
import tkinter as tk

import time
from functools import partial

question_labels = None

def tksleep(t):
    # adopted from https://stackoverflow.com/questions/74214619/how-to-use-tkinter-after-method-to-delay-a-loop-instead-time-sleep
    ms = int(t*1000)
    root = tk._get_default_root()
    var = tk.IntVar(root)
    root.after(ms, lambda: var.set(1))
    root.wait_variable(var)


def show_stuff(gui, questions_asked, target_values, questions_dict, response_values):

    for index, one_value in enumerate(target_values):
        question = questions_asked[index]
        response_string = response_values[index]

        response_string.set("Bot is thinking...")
        tksleep(random.choice([0.5, 1, 1.5, 2]))

        if one_value.get() == "YES":
            response_string.set(questions_dict[question][0])
        elif one_value.get() == "NO":
            response_string.set(questions_dict[question][0])
        else:
            response_string.set("Talk to me :(")


def textWindow(master):
    gui = Toplevel(master)

    # set the background colour of GUI window

    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Talk With Nobody")

    # set the configuration of GUI window
    gui.geometry("900x800")
    questions_dict = {
        'Do you have a best friend?':["Obviously...", "Go outside."],
        'Do you have any siblings?':["Hope they aren't annoying", "Lucky..."], 
        'Are your brothers and sisters annoying?':["No shot sherlock", "Liar!"], 
        'Can you count to 1000?':["You are patient", "Let it stay that way"], 
        'Are you afraid of the dark?':["Good for you", "You gotta get over it eventually."], 
        'Do you have a favorite superhero?':["OK", "Find one!"], 
        'Do you know your mom’s and dad’s first names?':["OK Good", "You stupid!"], 
        'Do your parents ever embarrass you?':["Obviously", "You have got to be lying"], 
        'Do you have a favorite dinosaur?':["Dinosaur GRRR-George from Peppa Pig", "gr"], 
        'Do you know why the sky is blue?':["Good, you better", "2 words: Touch.Grass."], 
        'Can you spell onomatopoeia?':["Good.", "I hate that word too."], 
        'Have you ever lied to your parents?':["At least you're not lying here", "There we go again"], 
        'Do you like ice cream?':["Why would you not?", "Psychopath.."], 
        'Do you like broccoli?':["WHATT?", "Of course"], 
        'Have you ever won a contest?':["Yay!", "Go away. Loser"], 
        'Have you ever played on a sports team?':["Good, you better","What is grass?"],
        'Do you help your parents with chores?':["You better be","You terrible human"], 
        'Have you ever been grounded?':["At least your telling the truth","LIAR"], 
        'Do you have a favorite aunt or uncle?':["Just don't tell them","Saves you the trouble"], 
        'Have you ever broken a bone?':["OuCh!","You are careful"], 
        'Have you ever had stitches?':["They suck..","Lucky"], 
        'Do you know how to cook?':["Who let em cook?","You're scared of being fried :/"], 
        'Do you know how to ride a bike?':["Yeah no shot","How? Your are legit no smarter than a 2 year old :/"], 
        'Do you know how to swim?':["Nobody's drowning today!","I would advise staying away from boats then."], 
        'Do you like spiders?':["You are the minority here.","I respect that."], 
        'Have you ever been to summer camp?':["Ok","How do you spend your summers then?"], 
        'Do you have an imaginary friend?':["Because you have no friends ahahaaa","You have friends :)"], 
        'Have you ever caught a fish?':["Yay","Bro.."], 
        'Have you ever been to a sleepover?':["Typical...","Maybe because you have no friends ahahahah"], 
        'Have you ever seen a lion up close?':["Hes super spookifying I know","Good, make it stay that way"], 
        'Can you make a dolphin noise?':["BOY WHAT!?!?","You are still sane :)"], 
        'Have you ever moved to a new city?':["Who hasn't?","Ain't no way"], 
        'Have you ever read a 100 page book?':["Good, you better have","You are stupid IQ = 21 https://www.youtube.com/watch?v=iF9Xf2ilKO8"]
    }
    
    cow(gui,questions_dict)
    redo = Button(gui, text="Do it again", command=partial(cow, gui, questions_dict)).grid(row=10, column=1)

def cow(gui,questions_dict):
    global question_labels

    questions_list = list(questions_dict.keys())
    questions_asked = random.sample(questions_list, 5)
    target_values = [] 

    # https://stackoverflow.com/questions/21592630/why-do-my-tkinter-widgets-get-stored-as-non
    for i in range(5):
        aa = questions_asked[i]
        question_label=Label(gui, text=aa).grid(row =i, column = 0)

        target_value_1 = StringVar()
        target_value_1.set("None") # default value

        w = OptionMenu(gui, target_value_1, "YES", "NO").grid(row =i, column = 1)
        target_values.append(target_value_1)

    labels_for_response = []
    response_values = []
    for index, one_value in enumerate(target_values):

        response_string = StringVar()
        response_string.set("Click respond to get response")
        response_values.append(response_string)

        response = Label(gui, textvariable=response_string).grid(row=index, column= 2)
        labels_for_response.append(response)

    responde= Button(gui, text="Respond", command=partial(show_stuff, gui, questions_asked, target_values, questions_dict, response_values)
                         ).grid(row=10, column=0)
