import turtle as trtl

def main():
    #create turtle and set up box
    gary = trtl.Turtle()
    box(gary)
    xpos = -500
    ypos = -300

    #draw the lines

    while (gary.ycor() < 330):
        gary.penup()
        gary.goto(xpos, -300)
        gary.pendown()
        gary.goto(480, ypos+10)
        gary.penup()
        xpos += 15.4
        ypos += 10

    xpos = 480
    ypos = -300
    gary.goto(480, ypos)
    while (gary.ycor() < 330):
        gary.penup()
        gary.goto(xpos, -300)
        gary.pendown()
        gary.goto(-500, ypos+10)
        gary.penup()
        xpos -= 15.4
        ypos += 10

    xpos = -500
    ypos = 330
    gary.goto(-500, ypos)
    while (gary.ycor() > -300):
        gary.penup()
        gary.goto(xpos, 330)
        gary.pendown()
        gary.goto(480, ypos - 10)
        gary.penup()
        xpos += 15.4
        ypos -= 10

    xpos = 480
    ypos = 330
    gary.goto(480, ypos)
    while (gary.ycor() > -300):
        gary.penup()
        gary.goto(xpos, 330)
        gary.pendown()
        gary.goto(-500, ypos - 10)
        gary.penup()
        xpos -= 15.4
        ypos -= 10




    wn = trtl.Screen()
    wn.mainloop()

def box(gary):
    xpos = -500
    ypos = -300
    gary.speed(0)
    gary.penup()
    gary.goto(xpos,ypos)
    gary.pendown()
    gary.goto(xpos+980, ypos)
    gary.goto(xpos+980, ypos+630)
    gary.goto(xpos, ypos+630)
    gary.goto(xpos, ypos)



if __name__ == "__main__":
    main()