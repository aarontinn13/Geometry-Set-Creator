from abc import ABC, abstractmethod
import tkinter as tk
import math

class Drawable(ABC):

    @abstractmethod
    def __contains__(self, item):
        pass

    def __and__(self, other):
        return Intersection(self, other)

    def __or__(self, other):
        return Union(self, other)

    def __sub__(self, other):
        return Difference(self, other)

    def draw(self, canvas):
        for i in range(-CANVAS_HEIGHT,CANVAS_HEIGHT):
            for j in range(-CANVAS_WIDTH,CANVAS_WIDTH):
                if (i,-j) in self:
                    draw_pixel(canvas,i+250,j+250)


class Circle(Drawable):

    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def __contains__(self, point):
        pythagorean = math.sqrt((self.x-point[0])**2+(self.y-point[1])**2)
        #can we assume on edge?
        if pythagorean < self.r:
            return True
        else:
            return False

class Rectangle(Drawable):

    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __contains__(self, point):
        if self.x0 < point[0] < self.x1 and self.y0 < point[1] < self.y1:
            #can we assume on edge?
            #can we assume x1,y1 greater than x0,y0
            return True
        else:
            return False

class Intersection(Drawable):

    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        if point in self.shape1 and point in self.shape2:
            return True
        else:
            return False

class Union(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        if point in self.shape1 or point in self.shape2:
            return True
        else:
            return False

class Difference(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    def __contains__(self, point):
        if point in self.shape1 and point not in self.shape2:
            return True
        else:
            return False



CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def draw_pixel(canvas, x, y, color='#FF0000'):
    """Draw a pixel at (x,y) on the given canvas"""
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def main(shape):
    """Create a main window with a canvas to draw on"""

    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Render the user-defined shape

    # TODO: Insert your code here!

    shape.draw(canvas)
    draw_pixel(canvas, 180, 150)
    draw_pixel(canvas, 320, 150)

    # Start the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)

    tk.mainloop()

if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    head = Circle(0, 0, 200)
    left_eye = Circle(-70, 100, 20)
    right_eye = Circle(70, 100, 20)
    mouth = Rectangle(-90, -80, 90, -60)
    happy_face = head - left_eye - right_eye - mouth


    main(happy_face)
