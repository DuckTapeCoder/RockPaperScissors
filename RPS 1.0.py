#Imports
import turtle as trtl
import random

#Setup
text_style = ("Arial", 40, "bold")
text_style2 = ("Arial", 15, "bold")
screen = trtl.Screen()
trtl.title("Rock Paper Scissors")
screen.setup(800,800)
screen.bgcolor("grey")

#Create Writer
writer = trtl.Turtle()
writer.penup()
writer.hideturtle()
writer.speed(0)

resultWriter = trtl.Turtle()
resultWriter.penup()
resultWriter.hideturtle()
resultWriter.speed(0)
resultWriter.goto(-300, -100)


#Create Rock
rock = trtl.Turtle()
rock.shape("circle")
rock.turtlesize(3)
rock.penup()
rock.speed(0)

#Create Paper
paper = trtl.Turtle()
paper.shape("square")
paper.turtlesize(3)
paper.penup()
paper.speed(0)

#Create Scissors
scissors = trtl.Turtle()
scissors.shape("arrow")
scissors.turtlesize(3)
scissors.penup()
scissors.speed(0)

scissors2 = trtl.Turtle()
scissors2.shape("arrow")
scissors2.turtlesize(3)
scissors2.penup()
scissors2.speed(0)
scissors2.left(180)

#Organize Screen
writer.goto(-300,100)
writer.write("ROCK", font=text_style)
rock.goto(-220, 70)
writer.goto(-125, 100)
writer.write("PAPER", font=text_style)
paper.goto(-25, 70)
writer.goto(75, 100)
writer.write("SCISSORS", font=text_style)
scissors.goto(185, 70)
scissors2.goto(215, 70)


#Record
w = 0
l = 0
t = 0
ai = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]

#Functions
def rockPicked(x,y):
    global w
    global l
    global t
    rock.speed(0.2)
    rock.color("grey")
    rock.color("black")
    rock.speed(0)
    cpuChoice = ai[random.randint(0, len(ai) - 1)]
    if cpuChoice == 1:
        cpuChoice = "rock"
        t += 1
    elif cpuChoice == 2:
        cpuChoice = "paper"
        l += 1
    else:
        cpuChoice = "scissors"
        w += 1
    for i in range(3):
        ai.append(2)
    if 3 in ai:
        ai.remove(3)
    writeResults("rock", cpuChoice)

def paperPicked(x,y):
    global w
    global l
    global t
    paper.speed(0.2)
    paper.color("grey")
    paper.color("black")
    paper.speed(0)
    cpuChoice = ai[random.randint(0, len(ai) - 1)]
    if cpuChoice == 1:
        cpuChoice = "rock"
        w += 1
    elif cpuChoice == 2:
        cpuChoice = "paper"
        t += 1
    else:
        cpuChoice = "scissors"
        l += 1
    for i in range(3):
        ai.append(3)
    if 1 in ai:
        ai.remove(1)
    writeResults("paper", cpuChoice)

def scissorsPicked(x,y):
    global w
    global l
    global t
    scissors.speed(0.2)
    scissors2.speed(0.2)
    scissors.color("grey")
    scissors2.color("grey")
    scissors.color("black")
    scissors2.color("black")
    scissors.speed(0)
    scissors2.speed(0)
    cpuChoice = ai[random.randint(0, len(ai) - 1)]
    if cpuChoice == 1:
        cpuChoice = "rock"
        l += 1
    elif cpuChoice == 2:
        cpuChoice = "paper"
        w += 1
    else:
        cpuChoice = "scissors"
        t += 1
    for i in range(3):
        ai.append(1)
    if 2 in ai:
        ai.remove(2)
    writeResults("scissors", cpuChoice)

#Write Our Results
def writeResults(playerChoice, cpuChoice):
    resultWriter.clear()
    resultWriter.write("You Chose " + playerChoice.upper() + ", the CPU Chose " + cpuChoice.upper() + ". Record: " + str(w) + "-" + str(l) + "-" + str(t), font=text_style2)



#Game Loop
rock.onclick(rockPicked)
paper.onclick(paperPicked)
scissors.onclick(scissorsPicked)
scissors2.onclick(scissorsPicked)


trtl.Screen().mainloop()