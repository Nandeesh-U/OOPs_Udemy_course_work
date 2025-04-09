from PIL import Image
import numpy as np

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        img_array = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        img_array[:] = self.color
        print(img_array)
        img = Image.fromarray(img_array, 'RGB')
        img.save(imagepath)