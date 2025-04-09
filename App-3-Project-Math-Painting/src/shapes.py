from PIL import Image
import numpy as np

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        # draw the square on the canvas
        canvas.img_array[self.x:self.x + self.side, self.y:self.y + self.side] = self.color

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        # draw the rectangle on the canvas
        canvas.img_array[self.x:self.x + self.height, self.y:self.y + self.width] = self.color

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create an array of zeros with the specified width and height
        # and fill it with the specified color
        self.img_array = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.img_array[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.img_array, 'RGB')
        img.save(imagepath)