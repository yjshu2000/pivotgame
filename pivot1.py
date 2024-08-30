'''
heyyyy we're back haha
with all new oop approach :3
...also github hopefully.

stuff to add:
x put a big arrow in the middle indicating rotation direction, in the bg
x change direction each click
- add score counter
- add new game restart (and make sure to fully end prev game)
'''

##############################################################################

from random import randint
import tkinter as tk
from time import sleep
import mathextras as pvm #pivot math? idk man i just want a short name
from math import sin, cos, sqrt

class Orbiter:
    """
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
    #returns bool
    #if collided, moves self to new location
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

class BGArrow:
    """
    just gimme the width and height of the screen!!
    and the screen.
    tuples: 0 is CCW, 1 is CW
    """ #maybe add clr dependent on bgclr someday
    def __init__(self, WIDTH, HEIGHT, Screen):
        self.COLOUR = "snow3"
        self.CENX = WIDTH // 2
        self.CENY = HEIGHT // 2
        self.RAD = min(WIDTH, HEIGHT) // 3
        self.startang = (45, 225) #you better not change this...
            #rest of the code kinda depends on startang being +/- 45
        collapsed = int(sqrt(self.RAD ** 2 / 2)) #idk what to name it ok ToT
        self.arwx0 = (self.CENX + collapsed,
                      self.CENX - collapsed)
        self.arwy0 = (self.CENY + collapsed,
                      self.CENY + collapsed)
        self.arwx1 = (self.arwx0[0] - self.RAD // 3,
                      self.arwx0[1] + self.RAD // 3)
        self.arwy1 = (self.arwy0[0], self.arwy0[1])
        self.arwx2 = (self.arwx0[0], self.arwx0[1])
        self.arwy2 = (self.arwy0[0] + self.RAD // 3,
                      self.arwy0[1] + self.RAD // 3)
        self.screen = Screen
        self.dir = 0 #0 or 1
        self.arc = self.screen.create_arc(
            self.CENX - self.RAD, self.CENY - self.RAD,
            self.CENX + self.RAD, self.CENY + self.RAD,
            start = self.startang[self.dir], extent = 270, style = tk.ARC,
            width = self.RAD // 10, outline = self.COLOUR, tag = "arrow")
        self.arw = self.screen.create_line(
            self.arwx1[self.dir], self.arwy1[self.dir],
            self.arwx0[self.dir], self.arwy0[self.dir],
            self.arwx2[self.dir], self.arwy2[self.dir],
            fill = self.COLOUR, width = self.RAD // 10, tag = "arrow")

    def flip(self):
        self.screen.delete("arrow")
        self.dir = 1 - self.dir #crazy toggle tysm cgpt
        self.arc = self.screen.create_arc(
            self.CENX - self.RAD, self.CENY - self.RAD,
            self.CENX + self.RAD, self.CENY + self.RAD,
            start = self.startang[self.dir], extent = 270, style = tk.ARC,
            width = self.RAD // 10, outline = self.COLOUR, tag = "arrow")
        self.arw = self.screen.create_line(
            self.arwx1[self.dir], self.arwy1[self.dir],
            self.arwx0[self.dir], self.arwy0[self.dir],
            self.arwx2[self.dir], self.arwy2[self.dir],
            fill = self.COLOUR, width = self.RAD // 10, tag = "arrow")
        self.screen.tag_lower("arrow")

#--------

#class ScoreText:
    #...

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
        self.clockwise = False
        self.orbiters = []
        #tkinter stuff
        self.root = root
        self.screen = tk.Canvas(root, width = self.WIDTH, height = self.HEIGHT,
                                background = self.BGCOLR)
        self.screen.bind("<Button-1>", self.click)
        self.screen.bind('<ButtonRelease-1>', self.released)
        self.screen.pack()
        self.screen.focus_set()
        
        #initialize arrow
        self.bgarrow = BGArrow(self.WIDTH, self.HEIGHT, self.screen)
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
        self.clockwise = not self.clockwise
        self.bgarrow.flip()

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
                if self.clockwise:
                    newlocx = (orb.r * cos(t / 20 + orb.theta) + x)
                    newlocy = (orb.r * sin(t / 20 + orb.theta) + y)
                else:
                    newlocx = (orb.r * cos(-t / 20 + orb.theta) + x)
                    newlocy = (orb.r * sin(-t / 20 + orb.theta) + y)
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

