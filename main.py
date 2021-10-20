import turtle as trtl

def main():
    #create turtle and set up box
    gary = trtl.Turtle()
    box(gary)

    #draw the lines
    if (gary.xcor() <= 130):
        gary.penup()
        gary.goto(-500, -300)
        gary.pendown()
        gary.forward(xpos + 10)
        gary.goto(130, ypos+10)
        xpos += 10
        ypos += 10

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