import numpy as np
from PIL import Image
from shapes import Square, Rectangle, Canvas

data = np.zeros((100, 160, 3), dtype=np.uint8)
data[:] = (255, 255, 255)  # Fill with white color
img = Image.fromarray(data, 'RGB')
img.save('files\canvas.png')

the_canvas = Canvas(100, 160, (255, 255, 255))
rec1=Rectangle(65,85,40,30,[255,0,0])
rec1.draw(the_canvas)
sq1 = Square(20, 5, 35, [0, 255, 0])
sq1.draw(the_canvas)
the_canvas.make('files\canvas2.png')