# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
from functools import partial

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(one_key: str, event=None):
    # point out the global expression variable
    global expression
    global equation

    # concatenation of string
    if one_key == "<BackSpace>":
        if len(expression) >= 1:
            expression = expression[:-1]
    else:
        expression = expression + one_key

    # update the expression by using set method
    equation.set(expression)



# Function to evaluate the final expression
def equalpress(event=None):
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        global expression_backup

        expression_backup = expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


def scientific_conversion():
    global equation
    global expression
    global expression_backup

    equation_value = equation.get()

    # if it is "error", do nothing
    if equation_value == " error ":
        return
    
    # only applies when equal is pressed
    if expression != "":
        return
    
    total = float(equation_value)

    if "e" not in equation_value:
        total_str = format(total, 'e')
    else:
        try:
            total_str = str(eval(expression_backup))
        except:
            total_str = " error "


    equation.set(total_str)
    
    
# Function to clear the contents
# of text entry box
def clear(event=None):
    global expression
    expression = ""
    equation.set("")


def basicWindow(master):

    global equation
    
    gui = Toplevel(master)

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("540x300")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation, state="disabled")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=3, row=4, ipadx=70)

    buttons_dict = {}
    k = 5
    buttons_dict["1"] = ["   1   ", "black", "red", k, 0]
    buttons_dict["2"] = ["   2   ", "black", "red", k, 1]
    buttons_dict["3"] = ["   3   ", "black", "red", k, 2]
    buttons_dict["4"] = ["   4   ", "black", "red", k+1, 0]
    buttons_dict["5"] = ["   5   ", "black", "red", k+1, 1]
    buttons_dict["6"] = ["   6   ", "black", "red", k+1, 2]
    buttons_dict["7"] = ["   7   ", "black", "red", k+2, 0]
    buttons_dict["8"] = ["   8   ", "black", "red", k+2, 1]
    buttons_dict["9"] = ["   9   ", "black", "red", k+2, 2]
    buttons_dict["0"] = ["   0   ", "black", "red", k+3, 0]
    buttons_dict["-"] = ["   -   ", "black", "red", k+3, 1]
    buttons_dict["+"] = ["   +   ", "black", "red", k+3, 2]
    buttons_dict["*"] = ["   *   ", "black", "red", k+4, 0]
    buttons_dict["/"] = ["   /   ", "black", "red", k+4, 1]
    buttons_dict["."] = ["   .   ", "black", "red", k+4, 2]
    buttons_dict["<BackSpace>"] = ["  Backspace  ", "black", "red", k+5, 0]


    basic_mode_buttons = {}
    for button_name in buttons_dict:
        my_button = Button(
            gui,
            text=buttons_dict[button_name][0],
            fg=buttons_dict[button_name][1],
            bg=buttons_dict[button_name][2],
            command=partial(press, button_name),
            height=1,
            width=9
        )
        gui.bind(button_name, partial(press, button_name))

        my_button.grid(row=buttons_dict[button_name][3], column=buttons_dict[button_name][4])
        basic_mode_buttons[button_name] = my_button




    clear_button = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=9)
    clear_button.grid(row=k+5, column=1)
    basic_mode_buttons['Clear'] = clear_button
    gui.bind("<Delete>", partial(clear))

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=9)
    equal.grid(row=k+5, column=2)
    basic_mode_buttons["="] = equal
    gui.bind("=", partial(equalpress))

    scientific_notation = Button(gui, text=' Toggle e+ ', fg='black', bg='red',
                   command=scientific_conversion, height=1, width=9)
    scientific_notation.grid(row=k+6, column=0)
    basic_mode_buttons["e+"] = scientific_notation

    # start the GUI
    gui.mainloop()

