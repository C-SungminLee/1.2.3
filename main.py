import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

# Setting up all the turtles that look like an apple for every letter of the Alphabet

applea = trtl.Turtle() 
appleb = trtl.Turtle()
applec = trtl.Turtle()
appled = trtl.Turtle()
applee = trtl.Turtle()
applef = trtl.Turtle()
appleg = trtl.Turtle()
appleh = trtl.Turtle()
applei = trtl.Turtle()
applej = trtl.Turtle()
applek = trtl.Turtle()
applel = trtl.Turtle()
applem = trtl.Turtle()
applen = trtl.Turtle()
appleo = trtl.Turtle()
applep = trtl.Turtle()
appleq = trtl.Turtle()
appler = trtl.Turtle()
apples = trtl.Turtle()
applet = trtl.Turtle()
appleu = trtl.Turtle()
applev = trtl.Turtle()
applew = trtl.Turtle()
applex = trtl.Turtle()
appley = trtl.Turtle()
applez = trtl.Turtle()

#Hiding the apple turtles

applea .hideturtle()
appleb .hideturtle()
applec .hideturtle()
appled .hideturtle()
applee .hideturtle()
applef .hideturtle()
appleg .hideturtle()
appleh .hideturtle()
applei .hideturtle()
applej .hideturtle()
applek .hideturtle()
applel .hideturtle()
applem .hideturtle()
applen .hideturtle()
appleo .hideturtle()
applep .hideturtle()
appleq .hideturtle()
appler .hideturtle()
apples .hideturtle()
applet .hideturtle()
appleu .hideturtle()
applev .hideturtle()
applew .hideturtle()
applex .hideturtle()
appley .hideturtle()
applez .hideturtle()


# Setting up all the turtles that write the letters for every letter of the Alphabet


drawera = trtl.Turtle()
drawerb = trtl.Turtle()
drawerc = trtl.Turtle()
drawerd = trtl.Turtle()
drawere = trtl.Turtle()
drawerf = trtl.Turtle()
drawerg = trtl.Turtle()
drawerh = trtl.Turtle()
draweri = trtl.Turtle()
drawerj = trtl.Turtle()
drawerk = trtl.Turtle()
drawerl = trtl.Turtle()
drawerm = trtl.Turtle()
drawern = trtl.Turtle()
drawero = trtl.Turtle()
drawerp = trtl.Turtle()
drawerq = trtl.Turtle()
drawerr = trtl.Turtle()
drawers = trtl.Turtle()
drawert = trtl.Turtle()
draweru = trtl.Turtle()
drawerv = trtl.Turtle()
drawerw = trtl.Turtle()
drawerx = trtl.Turtle()
drawery = trtl.Turtle()
drawerz = trtl.Turtle()

#Changing the color to white

drawera.color("white")
drawerb.color("white")
drawerc.color("white")
drawerd.color("white")
drawere.color("white")
drawere .color("white")
drawerf .color("white")
drawerg .color("white")
drawerh .color("white")
draweri .color("white")
drawerj .color("white")
drawerk .color("white")
drawerl .color("white")
drawerm .color("white")
drawern .color("white")
drawero .color("white")
drawerp .color("white")
drawerq .color("white")
drawerr .color("white")
drawers .color("white")
drawert .color("white")
draweru .color("white")
drawerv .color("white")
drawerw .color("white")
drawerx .color("white")
drawery .color("white")
drawerz .color("white")

drawera.hideturtle()
drawerb.hideturtle()
drawerc.hideturtle()
drawerd.hideturtle()
drawere.hideturtle()
drawerf .hideturtle()
drawerg .hideturtle()
drawerh .hideturtle()
draweri .hideturtle()
drawerj .hideturtle()
drawerk .hideturtle()
drawerl .hideturtle()
drawerm .hideturtle()
drawern .hideturtle()
drawero .hideturtle()
drawerp .hideturtle()
drawerq .hideturtle()
drawerr .hideturtle()
drawers .hideturtle()
drawert .hideturtle()
draweru .hideturtle()
drawerv .hideturtle()
drawerw .hideturtle()
drawerx .hideturtle()
drawery .hideturtle()
drawerz .hideturtle()

#Setting up all global variables

#Fall variable stops the user from "droping" apples until the apple they press dropped
global fall
fall = False

#number_of_apple variable shows how many of apples are on screen so only 5 stay on screen at most
global number_of_apple
number_of_apple = 0

#The list for all the letters a apple can have
global alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#letter variables to determine if the letter has been shown
global lettera
lettera = False
global letterb
letterb = False
global letterc
letterc = False
global letterd
letterd = False
global lettere
lettere = False
global letterf
letterf = False
global letterg
letterg = False
global letterh
letterh = False
global letteri
letteri = False
global letterj
letterj = False
global letterk
letterk = False
global letterl
letterl = False
global letterm
letterm = False
global lettern
lettern = False
global lettero
lettero = False
global letterp
letterp = False
global letterq
letterq = False
global letterr
letterr = False
global letters
letters = False
global lettert
lettert = False
global letteru
letteru = False
global letterv
letterv = False
global letterw
letterw = False
global letterx
letterx = False
global lettery
lettery = False
global letterz
letterz = False

#function that draws the apple
def draw_apple(active_apple,drawer,letter):
  global alphabet
  global number_of_apple
  if len(alphabet) > 0:
    active_apple.hideturtle()
    active_apple.shape(apple_image)
    active_apple.pu()
    #random locaion for apple
    active_apple.setposition(rand.randint(-150,150), rand.randint(-50,150))
    
    drawer.pu()
    #writes the letter
    drawer.goto(active_apple.xcor()-16, active_apple.ycor()-35)
    active_apple.showturtle()
    drawer.write(letter, font=("Arial", 40, "bold")) 
    wn.update()

def a():
  global fall
  global lettera
  global number_of_apple
  
  if fall == False and lettera == True:
    print("a")
    fall = True
    a = False
    number_of_apple = number_of_apple - 1
    applea.hideturtle()
    applea.showturtle()
    applea.penup()
    drawera.clear()
    applea.setposition(applea.xcor(), (-200))
    wn.update()
    applea.stamp()
    applea.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"a")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def b():
  global fall
  global letterb
  global number_of_apple
  
  if fall == False and letterb == True:
    print("b")
    fall = True
    b = False
    number_of_apple = number_of_apple - 1
    appleb.hideturtle()
    appleb.showturtle()
    appleb.penup()
    drawerb.clear()
    appleb.setposition(appleb.xcor(), (-200))
    wn.update()
    appleb.stamp()
    appleb.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"b")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def c():
  global fall
  global letterc
  global number_of_apple
  
  if fall == False and letterc == True:
    print("c")
    fall = True
    c = False
    number_of_apple = number_of_apple - 1
    applec.hideturtle()
    applec.showturtle()
    applec.penup()
    drawerc.clear()
    applec.setposition(applec.xcor(), (-200))
    wn.update()
    applec.stamp()
    applec.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"c")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def d():
  global fall
  global letterd
  global number_of_apple
  
  if fall == False and letterd == True:
    print("d")
    fall = True
    d = False
    number_of_apple = number_of_apple - 1
    appled.hideturtle()
    appled.showturtle()
    appled.penup()
    drawerd.clear()
    appled.setposition(appled.xcor(), (-200))
    wn.update()
    appled.stamp()
    appled.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"d")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def e():
  global fall
  global lettere
  global number_of_apple
  
  if fall == False and lettere == True:
    print("e")
    fall = True
    e = False
    number_of_apple = number_of_apple - 1
    applee.hideturtle()
    applee.showturtle()
    applee.penup()
    drawere.clear()
    applee.setposition(applee.xcor(), (-200))
    wn.update()
    applee.stamp()
    applee.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"e")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def f():
  global fall
  global letterf
  global number_of_apple
  
  if fall == False and letterf == True:
    print("f")
    fall = True
    f = False
    number_of_apple = number_of_apple - 1
    applef.hideturtle()
    applef.showturtle()
    applef.penup()
    drawerf.clear()
    applef.setposition(applef.xcor(), (-200))
    wn.update()
    applef.stamp()
    applef.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"f")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def g():
  global fall
  global letterg
  global number_of_apple
  
  if fall == False and letterg == True:
    print("g")
    fall = True
    g = False
    number_of_apple = number_of_apple - 1
    appleg.hideturtle()
    appleg.showturtle()
    appleg.penup()
    drawerg.clear()
    appleg.setposition(appleg.xcor(), (-200))
    wn.update()
    appleg.stamp()
    appleg.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"g")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def h():
  global fall
  global letterh
  global number_of_apple
  
  if fall == False and letterh == True:
    print("h")
    fall = True
    h = False
    number_of_apple = number_of_apple - 1
    appleh.hideturtle()
    appleh.showturtle()
    appleh.penup()
    drawerh.clear()
    appleh.setposition(appleh.xcor(), (-200))
    wn.update()
    appleh.stamp()
    appleh.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"h")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def i():
  global fall
  global letteri
  global number_of_apple
  
  if fall == False and letteri == True:
    print("i")
    fall = True
    i = False
    number_of_apple = number_of_apple - 1
    applei.hideturtle()
    applei.showturtle()
    applei.penup()
    draweri.clear()
    applei.setposition(applei.xcor(), (-200))
    wn.update()
    applei.stamp()
    applei.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"i")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def j():
  global fall
  global letterj
  global number_of_apple
  
  if fall == False and letterj == True:
    print("j")
    fall = True
    j = False
    number_of_apple = number_of_apple - 1
    applej.hideturtle()
    applej.showturtle()
    applej.penup()
    drawerj.clear()
    applej.setposition(applej.xcor(), (-200))
    wn.update()
    applej.stamp()
    applej.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"j")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def k():
  global fall
  global letterk
  global number_of_apple
  
  if fall == False and letterk == True:
    print("k")
    fall = True
    k = False
    number_of_apple = number_of_apple - 1
    applek.hideturtle()
    applek.showturtle()
    applek.penup()
    drawerk.clear()
    applek.setposition(applek.xcor(), (-200))
    wn.update()
    applek.stamp()
    applek.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"k")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def l():
  global fall
  global letterl
  global number_of_apple
  
  if fall == False and letterl == True:
    print("l")
    fall = True
    l = False
    number_of_apple = number_of_apple - 1
    applel.hideturtle()
    applel.showturtle()
    applel.penup()
    drawerl.clear()
    applel.setposition(applel.xcor(), (-200))
    wn.update()
    applel.stamp()
    applel.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"l")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def m():
  global fall
  global letterm
  global number_of_apple
  
  if fall == False and letterm == True:
    print("m")
    fall = True
    m = False
    number_of_apple = number_of_apple - 1
    applem.hideturtle()
    applem.showturtle()
    applem.penup()
    drawerm.clear()
    applem.setposition(applem.xcor(), (-200))
    wn.update()
    applem.stamp()
    applem.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"m")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def n():
  global fall
  global lettern
  global number_of_apple
  
  if fall == False and lettern == True:
    print("n")
    fall = True
    n = False
    number_of_apple = number_of_apple - 1
    applen.hideturtle()
    applen.showturtle()
    applen.penup()
    drawern.clear()
    applen.setposition(applen.xcor(), (-200))
    wn.update()
    applen.stamp()
    applen.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"n")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def o():
  global fall
  global lettero
  global number_of_apple
  
  if fall == False and lettero == True:
    print("o")
    fall = True
    o = False
    number_of_apple = number_of_apple - 1
    appleo.hideturtle()
    appleo.showturtle()
    appleo.penup()
    drawero.clear()
    appleo.setposition(appleo.xcor(), (-200))
    wn.update()
    appleo.stamp()
    appleo.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"o")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def p():
  global fall
  global letterp
  global number_of_apple
  
  if fall == False and letterp == True:
    print("p")
    fall = True
    p = False
    number_of_apple = number_of_apple - 1
    applep.hideturtle()
    applep.showturtle()
    applep.penup()
    drawerp.clear()
    applep.setposition(applep.xcor(), (-200))
    wn.update()
    applep.stamp()
    applep.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"p")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def q():
  global fall
  global letterq
  global number_of_apple
  
  if fall == False and letterq == True:
    print("q")
    fall = True
    q = False
    number_of_apple = number_of_apple - 1
    appleq.hideturtle()
    appleq.showturtle()
    appleq.penup()
    drawerq.clear()
    appleq.setposition(appleq.xcor(), (-200))
    wn.update()
    appleq.stamp()
    appleq.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"q")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def r():
  global fall
  global letterr
  global number_of_apple
  
  if fall == False and letterr == True:
    print("r")
    fall = True
    r = False
    number_of_apple = number_of_apple - 1
    appler.hideturtle()
    appler.showturtle()
    appler.penup()
    drawerr.clear()
    appler.setposition(appler.xcor(), (-200))
    wn.update()
    appler.stamp()
    appler.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"r")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def s():
  global fall
  global letters
  global number_of_apple
  
  if fall == False and letters == True:
    print("s")
    fall = True
    s = False
    number_of_apple = number_of_apple - 1
    apples.hideturtle()
    apples.showturtle()
    apples.penup()
    drawers.clear()
    apples.setposition(apples.xcor(), (-200))
    wn.update()
    apples.stamp()
    apples.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"s")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def t():
  global fall
  global lettert
  global number_of_apple
  
  if fall == False and lettert == True:
    print("t")
    fall = True
    t = False
    number_of_apple = number_of_apple - 1
    applet.hideturtle()
    applet.showturtle()
    applet.penup()
    drawert.clear()
    applet.setposition(applet.xcor(), (-200))
    wn.update()
    applet.stamp()
    applet.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"t")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def u():
  global fall
  global letteru
  global number_of_apple
  
  if fall == False and letteru == True:
    print("u")
    fall = True
    u = False
    number_of_apple = number_of_apple - 1
    appleu.hideturtle()
    appleu.showturtle()
    appleu.penup()
    draweru.clear()
    appleu.setposition(appleu.xcor(), (-200))
    wn.update()
    appleu.stamp()
    appleu.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"u")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def v():
  global fall
  global letterv
  global number_of_apple
  
  if fall == False and letterv == True:
    print("v")
    fall = True
    v = False
    number_of_apple = number_of_apple - 1
    applev.hideturtle()
    applev.showturtle()
    applev.penup()
    drawerv.clear()
    applev.setposition(applev.xcor(), (-200))
    wn.update()
    applev.stamp()
    applev.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"v")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def w():
  global fall
  global letterw
  global number_of_apple
  
  if fall == False and letterw == True:
    print("w")
    fall = True
    w = False
    number_of_apple = number_of_apple - 1
    applew.hideturtle()
    applew.showturtle()
    applew.penup()
    drawerw.clear()
    applew.setposition(applew.xcor(), (-200))
    wn.update()
    applew.stamp()
    applew.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"w")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def x():
  global fall
  global letterx
  global number_of_apple
  
  if fall == False and letterx == True:
    print("x")
    fall = True
    x = False
    number_of_apple = number_of_apple - 1
    applex.hideturtle()
    applex.showturtle()
    applex.penup()
    drawerx.clear()
    applex.setposition(applex.xcor(), (-200))
    wn.update()
    applex.stamp()
    applex.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"x")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def y():
  global fall
  global lettery
  global number_of_apple
  
  if fall == False and lettery == True:
    print("y")
    fall = True
    y = False
    number_of_apple = number_of_apple - 1
    appley.hideturtle()
    appley.showturtle()
    appley.penup()
    drawery.clear()
    appley.setposition(appley.xcor(), (-200))
    wn.update()
    appley.stamp()
    appley.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"y")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")

def z():
  global fall
  global letterz
  global number_of_apple
  
  if fall == False and letterz == True:
    print("z")
    fall = True
    z = False
    number_of_apple = number_of_apple - 1
    applez.hideturtle()
    applez.showturtle()
    applez.penup()
    drawerz.clear()
    applez.setposition(applez.xcor(), (-200))
    wn.update()
    applez.stamp()
    applez.hideturtle()
    fall = False
    print(number_of_apple)
    wn.onkeypress(None,"z")
    if number_of_apple == 0:
      print("tets")
      apple_generate()
      print("test2")


def apple_generate():
  global number_of_apple
  global alphabet
  global lettera
  global letterb
  global letterc
  global letterd
  global lettere
  global letterf
  global letterg
  global letterh
  global letteri
  global letterj
  global letterk
  global letterl
  global letterm
  global lettern
  global lettero
  global letterp
  global letterq
  global letterr
  global letters
  global lettert
  global letteru
  global letterv
  global letterw
  global letterx
  global lettery
  global letterz

  if len(alphabet) == 1:
    x = 0
    if alphabet[x] == "a" and number_of_apple < 5:
      draw_apple(applea,drawera,"a")
      number_of_apple +=1
      lettera = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "b" and number_of_apple < 5:
      draw_apple(appleb,drawerb,"b")
      number_of_apple +=1
      letterb = True
      alphabet.pop(x)
      print(number_of_apple)
      
    elif alphabet[x] == "c" and number_of_apple < 5:
      draw_apple(applec,drawerc,"c")
      number_of_apple +=1
      letterc = True
      alphabet.pop(x)  
      print(number_of_apple)

    elif alphabet[x] == "d" and number_of_apple < 5:
      draw_apple(appled,drawerd,"d")
      number_of_apple +=1
      letterd = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "e" and number_of_apple < 5:
      draw_apple(applee,drawere,"e")
      number_of_apple +=1
      lettere = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "f" and number_of_apple < 5:
      draw_apple(applef,drawerf,"f")
      number_of_apple +=1
      letterf = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "g" and number_of_apple < 5:
      draw_apple(appleg,drawerg,"g")
      number_of_apple +=1
      letterg = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "h" and number_of_apple < 5:
      draw_apple(appleh,drawerh,"h")
      number_of_apple +=1
      letterh = True
      alphabet.pop(x)
      print(number_of_apple)
    elif alphabet[x] == "i" and number_of_apple < 5:
      draw_apple(applei,draweri,"i")
      number_of_apple +=1
      letteri = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "j" and number_of_apple < 5:
      draw_apple(applej,drawerj,"j")
      number_of_apple +=1
      letterj = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "k" and number_of_apple < 5:
      draw_apple(applek,drawerk,"k")
      number_of_apple +=1
      letterk = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "l" and number_of_apple < 5:
      draw_apple(applel,drawerl,"l")
      number_of_apple +=1
      letterl = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "m" and number_of_apple < 5:
      draw_apple(applem,drawerm,"m")
      number_of_apple +=1
      letterm = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "n" and number_of_apple < 5:
      draw_apple(applen,drawern,"n")
      number_of_apple +=1
      lettern = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "o" and number_of_apple < 5:
      draw_apple(appleo,drawero,"o")
      number_of_apple +=1
      lettero = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "p" and number_of_apple < 5:
      draw_apple(applep,drawerp,"p")
      number_of_apple +=1
      letterp = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "q" and number_of_apple < 5:
      draw_apple(appleq,drawerq,"q")
      number_of_apple +=1
      letterq = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "r" and number_of_apple < 5:
      draw_apple(appler,drawerr,"r")
      number_of_apple +=1
      letterr = True
      alphabet.pop(x)
      print(number_of_apple)  

    elif alphabet[x] == "s" and number_of_apple < 5:
      draw_apple(apples,drawers,"s")
      number_of_apple +=1
      letters = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "t" and number_of_apple < 5:
      draw_apple(applet,drawert,"t")
      number_of_apple +=1
      lettert = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "u" and number_of_apple < 5:
      draw_apple(appleu,draweru,"u")
      number_of_apple +=1
      letteru = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "v" and number_of_apple < 5:
      draw_apple(applev,drawerv,"v")
      number_of_apple +=1
      letterv = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "w" and number_of_apple < 5:
      draw_apple(applew,drawerw,"w")
      number_of_apple +=1
      letterw = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "x" and number_of_apple < 5:
      draw_apple(applex,drawerx,"x")
      number_of_apple +=1
      letterx = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "y" and number_of_apple < 5:
      draw_apple(appley,drawery,"y")
      number_of_apple +=1
      lettery = True
      alphabet.pop(x)
      print(number_of_apple)  
    elif alphabet[x] == "z" and number_of_apple < 5:
      draw_apple(applez,drawerz,"z")
      number_of_apple +=1
      letterz = True
      alphabet.pop(x)
      print(number_of_apple)      

  if len(alphabet) > 1:
    for i in range(5):
      x =rand.randint(0,len(alphabet)-1)
      print(alphabet)
      print(len(alphabet))

      if alphabet[x] == "a" and number_of_apple < 5:
        draw_apple(applea,drawera,"a")
        number_of_apple +=1
        lettera = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "b" and number_of_apple < 5:
        draw_apple(appleb,drawerb,"b")
        number_of_apple +=1
        letterb = True
        alphabet.pop(x)
        print(number_of_apple)
        
      elif alphabet[x] == "c" and number_of_apple < 5:
        draw_apple(applec,drawerc,"c")
        number_of_apple +=1
        letterc = True
        alphabet.pop(x)  
        print(number_of_apple)

      elif alphabet[x] == "d" and number_of_apple < 5:
        draw_apple(appled,drawerd,"d")
        number_of_apple +=1
        letterd = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "e" and number_of_apple < 5:
        draw_apple(applee,drawere,"e")
        number_of_apple +=1
        lettere = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "f" and number_of_apple < 5:
        draw_apple(applef,drawerf,"f")
        number_of_apple +=1
        letterf = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "g" and number_of_apple < 5:
        draw_apple(appleg,drawerg,"g")
        number_of_apple +=1
        letterg = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "h" and number_of_apple < 5:
        draw_apple(appleh,drawerh,"h")
        number_of_apple +=1
        letterh = True
        alphabet.pop(x)
        print(number_of_apple)
      elif alphabet[x] == "i" and number_of_apple < 5:
        draw_apple(applei,draweri,"i")
        number_of_apple +=1
        letteri = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "j" and number_of_apple < 5:
        draw_apple(applej,drawerj,"j")
        number_of_apple +=1
        letterj = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "k" and number_of_apple < 5:
        draw_apple(applek,drawerk,"k")
        number_of_apple +=1
        letterk = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "l" and number_of_apple < 5:
        draw_apple(applel,drawerl,"l")
        number_of_apple +=1
        letterl = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "m" and number_of_apple < 5:
        draw_apple(applem,drawerm,"m")
        number_of_apple +=1
        letterm = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "n" and number_of_apple < 5:
        draw_apple(applen,drawern,"n")
        number_of_apple +=1
        lettern = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "o" and number_of_apple < 5:
        draw_apple(appleo,drawero,"o")
        number_of_apple +=1
        lettero = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "p" and number_of_apple < 5:
        draw_apple(applep,drawerp,"p")
        number_of_apple +=1
        letterp = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "q" and number_of_apple < 5:
        draw_apple(appleq,drawerq,"q")
        number_of_apple +=1
        letterq = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "r" and number_of_apple < 5:
        draw_apple(appler,drawerr,"r")
        number_of_apple +=1
        letterr = True
        alphabet.pop(x)
        print(number_of_apple)  
  
      elif alphabet[x] == "s" and number_of_apple < 5:
        draw_apple(apples,drawers,"s")
        number_of_apple +=1
        letters = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "t" and number_of_apple < 5:
        draw_apple(applet,drawert,"t")
        number_of_apple +=1
        lettert = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "u" and number_of_apple < 5:
        draw_apple(appleu,draweru,"u")
        number_of_apple +=1
        letteru = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "v" and number_of_apple < 5:
        draw_apple(applev,drawerv,"v")
        number_of_apple +=1
        letterv = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "w" and number_of_apple < 5:
        draw_apple(applew,drawerw,"w")
        number_of_apple +=1
        letterw = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "x" and number_of_apple < 5:
        draw_apple(applex,drawerx,"x")
        number_of_apple +=1
        letterx = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "y" and number_of_apple < 5:
        draw_apple(appley,drawery,"y")
        number_of_apple +=1
        lettery = True
        alphabet.pop(x)
        print(number_of_apple)  
      elif alphabet[x] == "z" and number_of_apple < 5:
        draw_apple(applez,drawerz,"z")
        number_of_apple +=1
        letterz = True
        alphabet.pop(x)
        print(number_of_apple)      
      else:
        print("done")
    else:
      print("done")
  

apple_generate()


wn.onkeypress(a,"a")
wn.onkeypress(b,"b")
wn.onkeypress(c,"c")
wn.onkeypress(d,"d")
wn.onkeypress(e,"e")
wn.onkeypress(f,"f")
wn.onkeypress(g,"g")
wn.onkeypress(h,"h")
wn.onkeypress(i,"i")
wn.onkeypress(j,"j")
wn.onkeypress(k,"k")
wn.onkeypress(l,"l")
wn.onkeypress(m,"m")
wn.onkeypress(n,"n")
wn.onkeypress(o,"o")
wn.onkeypress(p,"p")
wn.onkeypress(q,"q")
wn.onkeypress(r,"r")
wn.onkeypress(s,"s")
wn.onkeypress(t,"t")
wn.onkeypress(u,"u")
wn.onkeypress(v,"v")
wn.onkeypress(w,"w")
wn.onkeypress(x,"x")
wn.onkeypress(y,"y")
wn.onkeypress(z,"z")


wn.listen()


wn.mainloop()