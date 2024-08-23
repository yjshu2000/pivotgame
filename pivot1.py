'''
heyyyy we're back haha
with all new oop approach :3
...also github hopefully.

'''

##############################################################################

from random import randint
import tkinter as tk
from time import sleep
import mathextras as pvm #pivot math? idk man i just want a short name
from math import sin, cos

class Orbiter:
    """
    Fields??
    _x is orb's x
    _y is orb's y
    obj is the created orb object (I really hope that works)
    :p
    """
    def __init__(self, X, Y, screen, Theta, R):
        self.dotsize = 8
        self.colour = "red"
        self.x = X
        self.y = Y
        self.obj = screen.create_oval(X - self.dotsize, Y - self.dotsize,
                                      X + self.dotsize, Y + self.dotsize,
                                      fill = self.colour)
        self.theta = Theta
        self.r = R

    def __repr__(self):
        return "orb at ("+str(self.x)+", "+str(self.y)+")"

    def dele(self, screen):
        screen.delete(self.obj)

    def redraw(self, X, Y, screen, Theta, R):
        self.obj = screen.create_oval(X - self.dotsize, Y - self.dotsize,
                                      X + self.dotsize, Y + self.dotsize,
                                      fill = self.colour)
        self.x = X
        self.y = Y

#--------

class PivotGame:
    def __init__(self, root, wid, hei):
        self.WIDTH = wid
        self.HEIGHT = hei
        self.BGCOLR = "snow"
        self.CENX = self.WIDTH / 2
        self.CENY = self.HEIGHT / 2
        self.rotate = True
        self.orbiters = []
        self.root = root
        self.screen = tk.Canvas(root, width = self.WIDTH, height = self.HEIGHT,
                                background = self.BGCOLR)
        #screen stuff
        self.screen.bind("<Button-1>", self.click)
        self.screen.bind('<ButtonRelease-1>', self.released)
        self.screen.pack()
        self.screen.focus_set()

        #initialize first orbiter
        self.orb = Orbiter(randint(50, self.WIDTH - 50),
                           randint(50, self.HEIGHT - 50), self.screen, 0, 0)
        self.orbiters.append(self.orb)

    def click(self, event):
        self.rotate = True
        self.rotator(event.x, event.y)

    def released(self, event):
        self.rotate = False

    def crash(self):
        self.screen.create_text(self.WIDTH / 2, self.HEIGHT / 2, text="you\ncrashed", font="Tahoma 150",
                                justify="center", fill="red")

    def rotator(self, x, y):
        norbs = len(self.orbiters)
        for i in range(norbs):
            v = pvm.vectorize([self.orbiters[i].x, self.orbiters[i].y], [x, y])
            self.orbiters[i].theta = pvm.angdif([1, 0], v)
            self.orbiters[i].r = pvm.dist(x, y, self.orbiters[i].x, self.orbiters[i].y)
        
        t = 0
        while self.rotate:
            for i in range(norbs):
                currentorb = self.orbiters[i]
                self.orbiters[i].dele(self.screen)
                newlocx = (self.orbiters[i].r *
                           cos(t / 20 + self.orbiters[i].theta) + x)
                newlocy = (self.orbiters[i].r *
                           sin(t / 20 + self.orbiters[i].theta) + y)
                if (newlocx < 0 or newlocx > self.WIDTH or
                    newlocy < 0 or newlocy > self.HEIGHT):
                    self.crash()
                    break
                self.orbiters[i].redraw(newlocx, newlocy, self.screen,
                                       self.orbiters[i].theta, self.orbiters[i].r)
                self.screen.update()
            sleep(0.01)
            t += 1
        
        neworb = Orbiter(x, y, self.screen, 0, 0)
        self.orbiters.append(neworb)
        if norbs > 20:
            self.orbiters[0].dele(self.screen)
            self.orbiters.pop(0)
                

        

##############################################################################

WID = 800
HEI = 800

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pivot Game")
    game = PivotGame(root, WID, HEI)
    root.mainloop()

