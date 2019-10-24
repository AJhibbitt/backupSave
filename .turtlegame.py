from turtle import * 

myScreen = scoreTurtle.getscreen()
scoreTurtle.penup()
scoreTurtle.penup()
scoreTurtle.goto(myScreen.window_length() /2 - 200, myScreen.window_height()/2-50)
scoreTurtle.hideturtle()
score = 0

def updateScore()
    #scoreTurtle.clear()
    scoreTurtle.write("Score:" + str(score), False, "left", font=("Arial", 20, "normal"))

updateScore()

myScreen.mainloop()