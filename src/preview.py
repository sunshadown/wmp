import pyglet
from button import Button

class Preview:
    images = []
    max_preview = 10

    def __init__(self, image_paths, screen_x, screen_y):
        if len(image_paths) < self.max_preview:
            self.max_preview = len(image_paths)

        for i in range(self.max_preview):
            temp_image = pyglet.image.load(image_paths[i])
            temp = Button(screen_x + i * 120, screen_y, 100, 100, temp_image, "")
            self.images.append(temp)

    def update(self, dt):
        for i in self.images:
            i.update(dt)

    def render(self):
        for i in self.images:
            i.render()

    def onFocus(self, xc, yc):
        for i in self.images:
            i.focused(xc,yc)