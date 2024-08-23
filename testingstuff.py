


from tkinter import *
from math import sin, cos
from time import *
from random import *
from mathextras import *
WID = 800
HEI = 800

root = Tk()
screen = Canvas(root, width=WID, height=HEI, background="snow")
CENX = WID/2
CENY = HEI/2
dotsize = 8
rotate = True

def click(event):
    global rotate
    rotate = True
    rotator(event.x, event.y)

def released(event):
    global rotate
    rotate = False

screen.bind("<Button-1>", click)
screen.bind('<ButtonRelease-1>', released)

screen.pack()
screen.focus_set()


newlocx = randint(50,WID-50)
newlocy = randint(50,HEI-50)
orb = screen.create_oval(newlocx - dotsize, newlocy - dotsize,
                                newlocx + dotsize, newlocy + dotsize,
                                fill = "red")

def crash():
    screen.create_text(WID/2, HEI/2, text = "you\ncrashed", font = "Tahoma 150",
                       justify = "center", fill = "red")

def rotator(x, y):
    global orb, newlocx, newlocy
    #test = 4.71 #okay so this is in radians from -> and CW
    #oh, we need to find an angle. between two vectors:
    #1st vector is (1,0)
    #2nd vector needs to be converted: the one from (x,y) to (newlocx,newlocy)
    #v = vectorize([x,y],[newlocx,newlocy])
    v = vectorize([newlocx,newlocy],[x,y])
    theta = angdif([1,0],v)
    r = dist(x, y, newlocx, newlocy)
    t = 0
    while rotate:
        screen.delete(orb)
        newlocx = r * cos(t/20 + theta) + x  #...add phases here ig
        newlocy = r * sin(t/20 + theta) + y  #...^
        if ((newlocx < 0) or (newlocx > WID) or
            (newlocy < 0) or (newlocy > HEI)):
            crash()
            break
        orb = screen.create_oval(newlocx - dotsize, newlocy - dotsize,
                                newlocx + dotsize, newlocy + dotsize,
                                fill = "red")
        screen.update()
        sleep(0.01)
        t += 1

root.mainloop()


