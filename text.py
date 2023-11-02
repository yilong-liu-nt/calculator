import random
from tkinter import *
import time
from functools import partial



def show_stuff(gui, questions_asked, target_values, questions_dict, response_values):

    for index, one_value in enumerate(target_values):
        question = questions_asked[index]
        response_string = response_values[index]

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
        'Have you ever played on a sports team?':["",""],
        'Do you help your parents with chores?':["",""], 
        'Have you ever been grounded?':["",""], 
        'Do you have a favorite aunt or uncle?':["",""], 
        'Have you ever broken a bone?':["",""], 
        'Have you ever had stitches?':["",""], 
        'Do you know how to cook?':["",""], 
        'Do you know how to ride a bike?':["",""], 
        'Do you know how to swim?':["",""], 
        'Do you like spiders?':["",""], 
        'Have you ever been to summer camp?':["",""], 
        'Do you have an imaginary friend?':["",""], 
        'Have you ever caught a fish?':["",""], 
        'Have you ever been to a sleepover?':["",""], 
        'Have you ever seen a lion up close?':["",""], 
        'Can you make a dolphin noise?':["",""], 
        'Have you ever moved to a new city?':["",""], 
        'Have you ever read a 100 page book?':["",""]
    }
    
    questions_list = list(questions_dict.keys())

    questions_asked = random.sample(questions_list, 5)
    target_values = []  
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
        response_string.set("Bot is thinking....")
        response_values.append(response_string)

        response = Label(gui, textvariable=response_string).grid(row=index, column= 2)
        labels_for_response.append(response)

    responde= Button(gui, text="Respond", command=partial(show_stuff, gui, questions_asked, target_values, questions_dict, response_values)
                         ).grid(row=10, column=0)
    
