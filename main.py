import turtle as trtl

def main():
    #create turtle and set up box
    gary = trtl.Turtle()
    box(gary)
    xpos = -500
    ypos = -300

    #draw the lies
    #making the first box

    xpos = -500
    ypos = -300
    gary.goto(xpos, ypos)
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
    
    #making the second box
    box2(gary)

    xpos = -250
    ypos = -145
    gary.goto(xpos, ypos)
    while (gary.ycor() < 170):
        gary.penup()
        gary.goto(xpos, -145)
        gary.pendown()
        gary.goto(230, ypos+5)
        gary.penup()
        xpos += 7.7
        ypos += 5
    
    xpos = 230
    ypos = -145
    gary.goto(230, ypos)
    while (gary.ycor() < 170):
        gary.penup()
        gary.goto(xpos, -145)
        gary.pendown()
        gary.goto(-250, ypos+5)
        gary.penup()
        xpos -= 7.7
        ypos += 5

    xpos = -250
    ypos = 170
    gary.goto(-250, ypos)
    while (gary.ycor() > -145):
        gary.penup()
        gary.goto(xpos, 170)
        gary.pendown()
        gary.goto(230, ypos - 5)
        gary.penup()
        xpos += 7.7
        ypos -= 5

    xpos = 230
    ypos = 170
    gary.goto(230, ypos)
    while (gary.ycor() > -145):
        gary.penup()
        gary.goto(xpos, 170)
        gary.pendown()
        gary.goto(-250, ypos - 5)
        gary.penup()
        xpos -= 7.7
        ypos -= 5




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

def box2(gary):
    xpos = -250
    ypos = -145
    gary.speed(0)
    gary.penup()
    gary.goto(xpos,ypos)
    gary.pendown()
    gary.goto(xpos+480, ypos)
    gary.goto(xpos+480, ypos+315)
    gary.goto(xpos, ypos+315)
    gary.goto(xpos, ypos)



if __name__ == "__main__":
    main()