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
    x and y are coords of orb center
    obj is the created orb object (I really hope that works)
    theta and r are set on each click (as relative to pivot point)
    screen is the screen the orb is on!!! CONST
    """
    def __init__(self, X, Y, Screen, Theta = 0, R = 0):
        self.DOTSIZE = 8
        self.COLOUR = "red"
        self.x = X
        self.y = Y
        self.obj = Screen.create_oval(X - self.DOTSIZE, Y - self.DOTSIZE,
                                      X + self.DOTSIZE, Y + self.DOTSIZE,
                                      fill = self.COLOUR)
        self.theta = Theta
        self.r = R
        self.screen = Screen

    def __repr__(self):
        return "orb at ("+str(self.x)+", "+str(self.y)+")"

    def dele(self):
        self.screen.delete(self.obj)

    def redraw(self, X, Y):
        self.obj = self.screen.create_oval(X - self.DOTSIZE, Y - self.DOTSIZE,
                                      X + self.DOTSIZE, Y + self.DOTSIZE,
                                      fill = self.COLOUR)
        self.x = X
        self.y = Y

    def moov(self, X, Y):
        self.screen.move(self.obj, X - self.x, Y- self.y)
        self.x = X
        self.y = Y

    def set_theta_r(self, X, Y):
        v = pvm.vectorize([self.x, self.y], [X, Y])
        self.theta = pvm.angdif([1, 0], v)
        self.r = pvm.dist(X, Y, self.x, self.y)

#--------

class Target:
    """
    just gimme the width and height of the screen!!
    and the screen.
    """
    def __init__(self, WIDTH, HEIGHT, Screen):
        self.DOTSIZE = 8
        self.COLOUR = "cyan"
        self.randmin = 50
        self.randmax = WIDTH - 50
        self.randmay = HEIGHT - 50
        self.x = randint(self.randmin, self.randmax)
        self.y = randint(self.randmin, self.randmay)
        self.screen = Screen
        self.obj = Screen.create_oval(self.x - self.DOTSIZE, self.y - self.DOTSIZE,
                                      self.x + self.DOTSIZE, self.y + self.DOTSIZE,
                                      fill = self.COLOUR)

    #check if self is colliding with one specific orb
    def check_collision(self, orb):
        d = pvm.dist(self.x, self.y, orb.x, orb.y)
        collided = d < (self.DOTSIZE + orb.DOTSIZE)
        if collided:
            newx = randint(self.randmin, self.randmax)
            newy = randint(self.randmin, self.randmay)
            self.moov(newx, newy)
            return True
        else:
            return False

    def dele(self):
        self.screen.delete(self.obj)

    def moov(self, X, Y):
        self.screen.move(self.obj, X - self.x, Y- self.y)
        self.x = X
        self.y = Y
        

#--------

class PivotGame:
    def __init__(self, root, wid, hei):
        #const
        self.WIDTH = wid
        self.HEIGHT = hei
        self.BGCOLR = "snow"
        self.CENX = self.WIDTH / 2
        self.CENY = self.HEIGHT / 2
        self.SLEP = 0.01
        #var
        self.rotate = True
        self.orbiters = []
        #tkinter stuff
        self.root = root
        self.screen = tk.Canvas(root, width = self.WIDTH, height = self.HEIGHT,
                                background = self.BGCOLR)
        self.screen.bind("<Button-1>", self.click)
        self.screen.bind('<ButtonRelease-1>', self.released)
        self.screen.pack()
        self.screen.focus_set()

        #initialize first orbiter
        self.orb = Orbiter(randint(50, self.WIDTH - 50),
                           randint(50, self.HEIGHT - 50), self.screen)
        self.orbiters.append(self.orb)
        #initialize first target
        self.targ = Target(self.WIDTH, self.HEIGHT, self.screen)

    def click(self, event):
        self.rotate = True
        self.rotator(event.x, event.y)

    def released(self, event):
        self.rotate = False

    def crash(self):
        self.screen.create_text(self.WIDTH / 2, self.HEIGHT / 2,
                                text="you\ncrashed", font="Tahoma 150",
                                justify="center", fill="red")

    def rotator(self, x, y):
        norbs = len(self.orbiters)
        for orb in self.orbiters:
            orb.set_theta_r(x, y)
                    
        t = 0
        while self.rotate:
            for orb in self.orbiters:
                newlocx = (orb.r * cos(t / 20 + orb.theta) + x)
                newlocy = (orb.r * sin(t / 20 + orb.theta) + y)
                if (newlocx < 0 or newlocx > self.WIDTH or
                    newlocy < 0 or newlocy > self.HEIGHT):
                    self.crash()
                    break
                orb.moov(newlocx, newlocy)
                
                self.targ.check_collision(orb)
            self.screen.update()
            sleep(self.SLEP)
            t += 1
        
        neworb = Orbiter(x, y, self.screen)
        self.orbiters.append(neworb)
        if norbs > 20:
            self.orbiters[0].dele()
            self.orbiters.pop(0)
                

        

##############################################################################

WID = 800
HEI = 800

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pivot Game")
    game = PivotGame(root, WID, HEI)
    root.mainloop()

