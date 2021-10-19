import turtle as trtl

def main():
    #create turtle and set up box
    gary = trtl.Turtle()
    box(gary)

#draw the lines

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