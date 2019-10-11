import pyglet
from pyglet.gl import *
from model import Model

class Button(Model):
    def __init__(self, x, y, size_x, size_y, image):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.image = image
        self.image_x = image.width
        self.image_y = image.height
        self.sprite = pyglet.sprite.Sprite(img = self.image)
        self.sprite.x = x #- size_x / 2
        self.sprite.y = y #- size_y / 2 
        scale_x = float(self.image_x / size_x)
        scale_y = float(self.image_y / size_y)
        print(scale_x)
        print(scale_y)
        self.sprite.scale_x = scale_x
        self.sprite.scale_y = scale_y

    def render(self):
        self.sprite.draw()
    
    def update(self, dt):
        pass

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        npos_x = x -  self.size_x // 2
        npos_y = y - self.size_y //2
        self.sprite.x = npos_x
        self.sprite.y = npos_y
