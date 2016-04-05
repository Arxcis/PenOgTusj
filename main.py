from turtle import Turtle
from turtle import Screen


screen = Screen()

class Displ:

    def __init__(self):
        screen.bgcolor("blue")
        screen.register_shape("pen2.gif")


class Tegnesak(Turtle):

    farge = "hotpink"
    def __init__(self):
        super().__init__()
        self.speed(9)
        self.st()
        self.penup()
        self.shape('pen2.gif')
        self.ondrag(self.goto)
        self.pencolor(self.farge)
        self.pensize(5)
        self.shapesize(10)

        self.switch = 0
        self.switch2 = 0

    def loft_penn(self):
        if self.switch == 0: 
            self.pendown()
            self.switch = 1
        else:
            self.penup()
            self.switch = 0 

    def viskeler(self):
        if self.switch2 == 0:
            self.pencolor("blue")
            self.pensize(40)
            self.switch2 = 1
        elif self.switch2 == 1:
            self.pencolor(self.farge)
            self.pensize(5)
            self.switch2 = 0 

    def flush_screen(self):
        self.clear()

    def move_penn(self, direction):
        self.seth(direction)
        self.forward(20)




gfx = Displ()
penn = Tegnesak()


screen.onkey(penn.loft_penn, "space")
screen.onkey(penn.viskeler, "v")
screen.onkey(penn.flush_screen, "f")

def inject_direction(obj, direction):
    def set_move_penn():
        obj.move_penn(direction)
    return set_move_penn

screen.onkey(inject_direction(penn, 180), "Left")
screen.onkey(inject_direction(penn, 0), "Right")
screen.onkey(inject_direction(penn, 90), "Up")
screen.onkey(inject_direction(penn, 270), "Down")

screen.listen()

screen.mainloop()





