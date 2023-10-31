import random
from tkinter import *
def response(gui):
    response = Label(text=random.choice("yes", "no")).grid(row=1, column=0)
def textWindow(master):
    gui = Toplevel(master)

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Talk With Nobody")

    # set the configuration of GUI window
    gui.geometry("900x800")
    questions_list = ['Do you have a best friend?', 'Do you have any siblings?', 'Are your brothers and sisters annoying?', 'Can you count to 1000?', 'Are you afraid of the dark?', 'Do you have a favorite superhero?', 'Do you know your mom’s and dad’s first names?', 'Do your parents ever embarrass you?', 'Do you have a favorite dinosaur?', 'Do you know why the sky is blue?', 'Can you spell onomatopoeia?', 'Have you ever lied to your parents?', 'Do you like ice cream?', 'Do you like broccoli?', 'Have you ever won a contest?', 'Have you ever played on a sports team?', 'Do you help your parents with chores?', 'Have you ever been grounded?', 'Do you have a favorite aunt or uncle?', 'Have you ever broken a bone?', 'Have you ever had stitches?', 'Do you know how to cook?', 'Do you know how to ride a bike?', 'Do you know how to swim?', 'Do you like spiders?', 'Have you ever been to summer camp?', 'Do you have an imaginary friend?', 'Have you ever caught a fish?', 'Have you ever been to a sleepover?', 'Have you ever seen a lion up close?', 'Can you make a dolphin noise?', 'Have you ever moved to a new city?', 'Have you ever read a 100 page book?']
    
    for index, one_question in enumerate(questions_list):
        print(str(index+1) + ". " + one_question)

    for i in range(5):

        aa = random.choice(questions_list)
        question_label=Label(gui, text=aa).grid(row =i, column = 0)

        target_value_1 = StringVar(gui)
        target_value_1.set("None") # default value
        w = OptionMenu(gui, target_value_1, "YES", "NO").grid(row =i, column = 1)
