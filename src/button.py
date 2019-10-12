import pyglet
from pyglet.gl import *
from model import Model

class Button(Model):
    def __init__(self, x, y, size_x, size_y, image, text):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.image = image
        self.label = pyglet.text.Label(text,
                          font_name='Times New Roman',
                          font_size=18,
                          x = x, y = y,
                          anchor_x='center', anchor_y='center')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.image_x = image.width
        self.image_y = image.height
        self.sprite = pyglet.sprite.Sprite(img = self.image)
        self.sprite.x = x 
        self.sprite.y = y
        scale_x = 1.0
        scale_y = 1.0
        if size_x < self.sprite.width and size_y < self.sprite.height:
            scale_x = float(size_x / self.sprite.width)
            scale_y = float(size_y / self.sprite.height)
        
        self.sprite.scale_x = scale_x
        self.sprite.scale_y = scale_y

    def render(self):
        self.sprite.draw()
        self.label.draw()
    
    def update(self, dt):
        if self.mouse_callback is not None:
            if self.is_clicked:
                self.path = self.mouse_callback()
                self.is_clicked = False

        if self.is_focused:
            self.sprite.scale = 1.4
        else:
            self.sprite.scale = 1.0

    def clicked(self, xc, yc):
        temp_x = self.sprite.x - self.sprite.width // 2
        temp_y = self.sprite.y - self.sprite.height // 2
        
        if xc > temp_x and xc < temp_x + self.sprite.width:
            if yc > temp_y and yc < temp_y + self.sprite.height:
                self.is_clicked = True

    def focused(self, xc, yc):
        temp_x = self.sprite.x - self.sprite.width // 2
        temp_y = self.sprite.y - self.sprite.height // 2
        
        if xc > temp_x and xc < temp_x + self.sprite.width:
            if yc > temp_y and yc < temp_y + self.sprite.height:
                self.is_focused = True
                return
        self.is_focused = False

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.sprite.x = x
        self.sprite.y = y

    def SetMouseCallback(self,callback):
        self.mouse_callback = callback
