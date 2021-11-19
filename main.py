import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()


drawer = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
drawer5 = trtl.Turtle()

global fall
fall = False
global alphabet
alphabet = ["a","b","c","d","e","f","g"]
global letternum
global letter
letternum = ""
global turtle_list
turtle_list = [apple,apple2,apple3,apple4,apple5]
global letterlist
letterlist = []
letternum = rand.randint(0,len(alphabet)-1)
print (letternum)
letter = alphabet[letternum]

print (letter)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
'''
def draw_apple(active_apple,drawer):
  global alphabet
  if len(alphabet) > 0:
    reset_letter()
    active_apple.hideturtle()
    active_apple.shape(apple_image)
    active_apple.pu()
    active_apple.setposition(rand.randint(-150,150), rand.randint(-50,150))
    

    global letter
    drawer.pu()
    drawer.goto(active_apple.xcor()-18, active_apple.ycor()-40)
    active_apple.showturtle()

    drawer.write(letter, font=("Arial", 40, "bold")) 
    letterlist.append(letter)
    wn.update()

def drop_apple(apple,drawer):
  global fall
  global letter
  if fall == False:
    if letter == "a":
      fall = True
      apple.hideturtle()
      apple.showturtle()
      apple.penup()
      drawer.clear()
      apple.setposition(apple.xcor(), (-200))
      wn.update()
      apple.stamp()
      apple.hideturtle()

      wn.onkeypress(None,"a")
      reset_letter()
      drop_apple(apple,drawer)
      wn.onkeypress(drop_apple, letter)

      fall = False

    elif letter == "b":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"b")
        
        drop_apple(apple,drawer)
        wn.onkeypress(drop_apple, letter)

        fall = False
    elif letter == "c":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"c")
        
        drop_apple(apple,drawer)
        wn.onkeypress(drop_apple, letter)

        fall = False
    elif letter == "d":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"d")
        
        drop_apple(apple,drawer)
        wn.onkeypress(drop_apple, letter)

        fall = False
    elif letter == "e":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"e")
        
        drop_apple(apple,drawer)
        wn.onkeypress(drop_apple, letter)

        fall = False
    elif letter == "f":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"f")
        
        draw_apple(apple)
        wn.onkeypress(drop_apple, letter)

        fall = False
    elif letter == "g":
        fall = True
        apple.hideturtle()
        apple.showturtle()
        apple.penup()
        drawer.clear()
        apple.setposition(apple.xcor(), (-200))
        wn.update()
        apple.stamp()
        apple.hideturtle()
        apple.setposition(apple.xcor(), (apple.ycor()+200))
        apple.showturtle()
        wn.onkeypress(None,"g")
        
        draw_apple(apple)
        wn.onkeypress(drop_apple, letter)

        fall = False


def apple_select():
  drop_apple(apple,drawer)
def apple_select2():
  drop_apple(apple2,drawer2)
def apple_select3():
  drop_apple(apple3,drawer3)
def apple_select4():
  drop_apple(apple4,drawer4)
def apple_select5():
  drop_apple(apple5,drawer5)


#-----function calls-----

drawer.hideturtle()
drawer.color("white")

drawer2.hideturtle()
drawer2.color("white")

drawer3.hideturtle()
drawer3.color("white")

drawer4.hideturtle()
drawer4.color("white")

drawer5.hideturtle()
drawer5.color("white")


draw_apple(apple,drawer)
draw_apple(apple2,drawer2)
draw_apple(apple3,drawer3)
draw_apple(apple4,drawer4)
draw_apple(apple5,drawer5)



wn.onkeypress(apple_select, letterlist[0])
wn.onkeypress(apple_select2, letterlist[1])
wn.onkeypress(apple_select3, letterlist[2])
wn.onkeypress(apple_select4, letterlist[3])
wn.onkeypress(apple_select5, letterlist[4])
wn.listen()
'''


def draw_applea():
  global alphabet
  if len(alphabet) > 0:
    apple.hideturtle()
    apple.shape(apple_image)
    apple.pu()
    apple.setposition(rand.randint(-150,150), rand.randint(-50,150))
    

    global letter
    drawer.pu()
    drawer.goto(apple.xcor()-18, apple.ycor()-40)
    apple.showturtle()

    drawer.write("a", font=("Arial", 40, "bold")) 
    wn.update()

draw_applea()
    
wn.mainloop()
