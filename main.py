from turtle import Turtle
from turtle import Screen


bakgrunn = 'white'
screen = Screen()

class Canvas:

    def __init__(self, color='white'):
        
        self.color = color
        screen.bgcolor(self.color)

        # Import turtle shapes
        screen.register_shape('pen2.gif')
        screen.register_shape('red_tusj.gif')
        screen.register_shape('blue_tusj.gif')
        screen.register_shape('yellow_tusj.gif')

        # Set canvas borders
        self.max_h = screen.window_height() / 2
        self.min_h = screen.window_height() / 2 *(-1)
        self.max_w = screen.window_width() / 2
        self.min_w = screen.window_width() / 2 * (-1)


class Tegnesak(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(9)
        self.st()
        self.penup()

        self.switch = 0
        self.switch2 = 0

        self.init_input()

    def init_input(self):

        screen.onkey(self.loft_penn, "space")
        screen.onkey(self.flush_screen, "f")

        screen.onkey(self.inject_direction(180), "Left")
        screen.onkey(self.inject_direction(0), "Right")
        screen.onkey(self.inject_direction(90), "Up")
        screen.onkey(self.inject_direction(270), "Down")

    def inject_direction(self, direction):
        def set_move_penn():
            self.move_penn(direction)
        return set_move_penn

    def loft_penn(self):
        if self.switch == 0: 
            self.pendown()
            self.switch = 1
        else:
            self.penup()
            self.switch = 0 

    def viskeler(self, farge, bakgrunnsfarge=bakgrunn):
        if self.switch2 == 0:
            self.pencolor(bakgrunnsfarge)
            self.pensize(40)
            self.switch2 = 1
        elif self.switch2 == 1:
            self.pencolor(farge)
            self.pensize(5)
            self.switch2 = 0 

    def flush_screen(self):
        self.clear()

    def move_penn(self, direction):
        self.seth(direction)
        self.forward(20)


class Blyant(Tegnesak):
    def __init__(self):
        super().__init__()
        self.shape('pen2.gif')
        self.pensize(2)
        self.shapesize(10)

        self.init_blyantinput()

    def init_blyantinput(self):
        screen.onkey(self.blyantviskeler, 'v')

    def blyantviskeler(self):
        self.viskeler('black')

class Tusj(Tegnesak):
    def __init__(self, farge=1):
        super().__init__()
        self.tusjfarge = farge
        self.set_farge()
        self.pensize(8)
        self.init_tusjinput()

    def init_tusjinput(self):
        screen.onkey(self.tusjviskeler, 'v')
        screen.onkey(self.change_farge, 'c')
        
    def tusjviskeler(self):
        self.viskeler(self.tusjfarge)

    def change_farge(self):
        if self.tusjfarge == 1:
            self.tusjfarge = 2

        elif self.tusjfarge == 2:
            self.tusjfarge = 3

        elif self.tusjfarge == 3:
            self.tusjfarge = 1
      
        self.set_farge()

    def set_farge(self):
        if self.tusjfarge == 1:
            self.shape('red_tusj.gif')
            self.pencolor('red')

        elif self.tusjfarge == 2:
            self.shape('blue_tusj.gif')
            self.pencolor('blue')

        elif self.tusjfarge == 3:
            self.shape('yellow_tusj.gif')
            self.pencolor('yellow')


def select_object(obj):
        def switch_penn(): 
            penn = obj()
        return switch_penn


def main():
    gfx = Canvas(bakgrunn)

    screen.onkey(select_object(Blyant), '1')
    screen.onkey(select_object(Tusj), '2')

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()

"""
    session 15:20 - 16:46
"""


