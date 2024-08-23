#welp, separate extras for making objects I guess.



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
        

    
