from tkinter import *
import random

gui = Tk()
gui.title("Rock Paper Scissors")
gui.geometry("1000x1000")
going = True
cchoice = 0
w = 0
l = 0
t = 0
number = 0
rbutton = Button()
sbutton = Button()
pbutton = Button()
label1 = Label()





def rock():
    global w
    global l
    global t
    cchoice = random.randint(1,3)
    if cchoice == 1:
        t += 1
        label1 = Label(gui, text = "You chose ROCK, you're opponent chose ROCK, this round was a tie. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 2:
        l += 1
        label1 = Label(gui, text = "You chose ROCK, you're opponent chose PAPER, this round was a loss. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 3:
        w += 1
        label1 = Label(gui, text = "You chose ROCK, you're opponent chose SCISSORS, this round was a win. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()

def paper():
    global w
    global l
    global t
    cchoice = random.randint(1,3)
    if cchoice == 1:
        t += 1
        label1 = Label(gui, text = "You chose PAPER, you're opponent chose PAPER, this round was a tie. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 2:
        l += 1
        label1 = Label(gui, text = "You chose PAPER, you're opponent chose SCISSORS, this round was a loss. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 3:
        w += 1
        label1 = Label(gui, text = "You chose PAPER, you're opponent chose ROCK, this round was a win. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()

def scissors():
    global w
    global l
    global t
    cchoice = random.randint(1,3)
    if cchoice == 1:
        t += 1
        label1 = Label(gui, text = "You chose SCISSORS, you're opponent chose SCISSORS, this round was a tie. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 2:
        l += 1
        label1 = Label(gui, text = "You chose SCISSORS, you're opponent chose ROCK, this round was a loss. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()
    elif cchoice == 3:
        w += 1
        label1 = Label(gui, text = "You chose SCISSORS, you're opponent chose PAPER, this round was a win. Record: " + str(w) + "-" + str(l) + "-" + str(t)).pack()


rbutton = Button(gui, text = "ROCK", padx = 50, pady = 50, command = rock).pack()
pbutton = Button(gui, text = "PAPER", padx = 48, pady = 50, command = paper).pack()
sbutton = Button(gui, text = "SCISSORS", padx = 40, pady = 50, command = scissors).pack()




gui.mainloop()