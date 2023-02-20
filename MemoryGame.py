import random
import time
from tkinter import *
'''Programming Language Concepts Assignment Memory Game December 2019'''

INITIAL_START_VALUE = 3
FONT_SIZE = 15
WAIT_TIME = 1200
state = "explicit_show"
numbers = []
userInput = []
numberCount = INITIAL_START_VALUE
index = 0


window = Tk()
window.title("Remember blinking numbers!")
window.geometry('600x400')
text = Label(window, text="")
text.place(x=0, y=0)
inputLabel = Label(window, text="")
inputBox = ""
submitButton = ""

def goto_evaluate_input_state():
    global state
    state = "evaluate_input"
    window.after(100,stateManager)

def restart_game():
    global state
    global inputLabel
    global submitButton
    global numbers
    global numberCount
    global INITIAL_START_VALUE

    submitButton.grid_forget()
    inputLabel.grid_forget()
    numbers=[]
    state = "explicit_show"
    numberCount = INITIAL_START_VALUE
    window.after(100,stateManager)    

def next_level():
    global state
    global inputLabel
    global submitButton
    global numberCount
    global numbers

    submitButton.grid_forget()
    inputLabel.grid_forget()

    numbers=[]
    state = "generate_numbers"
    numberCount = numberCount + 1
    window.after(100,stateManager)  

def stateManager():
    global state
    global numbers
    global userInput
    global numberCount
    global index
    global FONT_SIZE
    global window
    global text
    global inputLabel
    global inputBox
    global submitButton
    global WAIT_TIME

    if state=="explicit_show":
        text = Label(window, text="Initial size is "+ str(INITIAL_START_VALUE))
        text.config(font=("Arial",FONT_SIZE))
        text.place(x=0, y=0)
        state="generate_numbers"
        window.after(1000, stateManager)

    elif state == "generate_numbers":
        text.destroy()
        print("generate_numbers")
        for x in range(numberCount):
            newNumber = random.randrange(1,100)
            numbers.append(newNumber)
        state = "show_numbers"
        text = Label(window, text="Let's start!")
        text.config(font=("Arial",FONT_SIZE))
        text.place(x=0, y=0)
        window.after(1000,stateManager) #goes to new state after 1000 miliseconds

    elif state == "show_numbers":
        print("show_numbers")
        text.destroy()
        if index != numberCount:
            xPos = random.randrange(1,(window.winfo_width()-(FONT_SIZE*2))) #so that the texts dont go out of window borders
            yPos = random.randrange(1,(window.winfo_height()-(FONT_SIZE*2)))
            text = Label(window, text=str(numbers[index]))
            text.config(font=("Consolas",FONT_SIZE))
            text.place(x=xPos, y=yPos)
            print("Number",numbers[index], "x:",xPos,"y:",yPos)
            window.after(WAIT_TIME,stateManager)
            index = index + 1
        else:
            state = "generate_user_input_field"
            index = 0 #for future use
            window.after(100,stateManager) #goes to new state after 100 miliseconds
        
    elif state == "generate_user_input_field":
        print("generate_user_input_field")
        inputLabel = Label(window, text="Enter numbers (separate only with ',' eg: 1,2,3)")
        inputLabel.grid(row=0, column=0)
        inputBox = Entry(window)
        inputBox.grid(row=0, column=1)
        inputBox.focus_set()
        submitButton = Button(window, text='Submit', command=goto_evaluate_input_state)
        submitButton.grid(row=0, column=2, pady=4)
    
    elif state == "evaluate_input":
        print("evaluate_input")
        inputLabel.grid_forget()
        inputBox.grid_forget()
        submitButton.grid_forget()
        userEntry = inputBox.get()
        userEntry = userEntry.split(',')
        if len(userEntry) != numberCount: #in case of input containing higher or lower number of items than we showed
            print("input count != expected count")
            state = "you_lose"
        else:
            for x in range(numberCount):
                state="you_win_this_time"
                if str(userEntry[x]) != str(numbers[x]):
                    print(userEntry[x]+" != "+str(numbers[x]))
                    state = "you_lose"
                    break
        window.after(100,stateManager)

    elif state == "you_win_this_time":
        print("you_win_this_time")
        inputLabel = Label(window, text="Good job!")
        inputLabel.grid(row=0, column=0)
        submitButton = Button(window, text='Next Level', command=next_level)
        submitButton.grid(row=0, column=1, pady=4)

    elif state == "you_lose":
        print("you_lose")
        inputLabel = Label(window, text="You lose!")
        inputLabel.grid(row=0, column=0)
        submitButton = Button(window, text='Restart', command=restart_game)
        submitButton.grid(row=0, column=1, pady=4)
    else:
        print("Unexpected state!")

stateManager()
window.mainloop()
