import math
from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def falls_in_rectangle(self, rectangle):
        lowleftpt = rectangle.lowleft
        uprightpt = rectangle.upright
        if lowleftpt.x < self.x < uprightpt.x and lowleftpt.y < self.y < uprightpt.y:
            return True
        else:
            return False


class GuiPoint(Point):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.pencolor('red')
        canvas.dot(size=5)
        canvas.penup()
        canvas.goto(50000, 50000)

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def __str__(self):
        return f"[({self.lowleft.x}, {self.lowleft.y}), ({self.upright.x}, {self.upright.y})]"

    def area(self):
        return abs(self.lowleft.x - self.upright.x) * abs(self.lowleft.y - self.upright.y)

class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)

gui_rectangle = GuiRectangle(
    Point(randint(100, 199), randint(100, 199)),
    Point(randint(200, 299), randint(200, 299))
)
print("Rectangle Coordinates:", gui_rectangle)

user_point = GuiPoint(float(input("Guess X: ")),
                      float(input("Guess Y: ")))
print("Your point was inside rectangle:", user_point.falls_in_rectangle(gui_rectangle))

my_turtle = turtle.Turtle()
gui_rectangle.draw(my_turtle)
user_point.draw(my_turtle)
turtle.done()

'''
point1 = Point(10, 23)
point2 = Point(15, 28)
point3 = Point(135, 24)
print(point1.distance(point2))
rectangle1 = Rectangle(point1, point2)
print(point3.falls_in_rectangle(rectangle1))

rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19))
)

print("Rectangle Coordinates:", rectangle)
user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))

print("Rectangle Coordinates:", rectangle)
user_area_guess = float(input("Guess the area of the rectangle: "))
if user_area_guess == rectangle.area():
    print("True")
else:
    print("False")

'''