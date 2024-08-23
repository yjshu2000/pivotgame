'''
gonna try making pivot game :p

2023-01-12: v0.1
    test orb is orbiting correctly!! just one tho ;w;
    next we should try making multiple orbiters... start collecting them...

2024-01-04: ??
    oh man we're finally back and have no clue what's going on
    last left off working on line 105
    
    OH GODS HOLY SHJT WE HAVE WORKING ORBITERS
    WE ARE ROTATING WHOLE GROUPS OF ORBS
    OMFG

    next: remove the first orb when orbs exceed 20
        (we're gonna need to figure out queue's ig)
    DONE YAY

    next: time to try and make targets ToT aaaaaaa

'''

##############################################################################

from random import *
from tkinter import *
from mathextras import *
from time import *
from objextras import *

WID = 800
HEI = 800

#dotsize = 8 #actually we moved this to inside the orb object

root = Tk()
root.title("Pivot Game")
screen = Canvas(root, width=WID, height=HEI, background="snow")
CENX = WID/2
CENY = HEI/2

orbiters = []
#targets = []

rotate = True

def click(event):
    global rotate
    rotate = True
    rotator(event.x, event.y)
    return

def released(event):
    global rotate
    rotate = False
    return

#we need to get rid of this and make this an object, probably
def newtarget():
    newlocx = randint(50,WID-50)
    newlocy = randint(50,HEI-50)
    target = screen.create_oval(newlocx - dotsize, newlocy - dotsize,
                                newlocx + dotsize, newlocy + dotsize,
                                fill = "cyan")
    return target

def crash():
    screen.create_text(WID/2, HEI/2, text = "you\ncrashed", font = "Tahoma 150",
                       justify = "center", fill = "red")

'''
def startrotat():
    norbs = len(orbiters)
    while holding:
        for i in range(norbs):
            pass
'''

orb = Orbiter(randint(50,WID-50), randint(50,HEI-50), screen, 0, 0)
orbiters.append(orb)

def rotator(x, y):
    global orb, orbiters 
    norbs = len(orbiters)
    for i in range(norbs):
        v = vectorize([orbiters[i].x,orbiters[i].y],[x,y])
        orbiters[i].theta = angdif([1,0],v)
        orbiters[i].r = dist(x, y, orbiters[i].x, orbiters[i].y)
    t = 0
    while rotate:
        for i in range(norbs):
            currentorb = orbiters[i]
            orbiters[i].dele(screen)
            newlocx = orbiters[i].r * cos(t/20 + orbiters[i].theta) + x
            newlocy = orbiters[i].r * sin(t/20 + orbiters[i].theta) + y
            if ((newlocx < 0) or (newlocx > WID) or
                (newlocy < 0) or (newlocy > HEI)):
                crash()
                break
            orbiters[i].redraw(newlocx, newlocy, screen,
                               orbiters[i].theta, orbiters[i].r)
            screen.update()
        sleep(0.01)
        t += 1
    neworb = Orbiter(x, y, screen, 0, 0)
    orbiters.append(neworb)
    if norbs > 20:
        orbiters[0].dele(screen)
        orbiters.pop(0)
    return


screen.bind("<Button-1>", click)
screen.bind('<ButtonRelease-1>', released)


screen.pack()
screen.focus_set()


#neworb = neworbiter()
#orbiters.append(neworb)

root.mainloop()
