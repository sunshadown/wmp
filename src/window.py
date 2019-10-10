import pyglet
from pyglet.gl import *

class Window:
    window = pyglet.window.Window(caption='WMP alpha version')
    window_x = None
    window_y = None
    label = pyglet.text.Label('WMP alpha',
                          font_name='Times New Roman',
                          font_size=36,
                          x=200, y=1000,
                          anchor_x='center', anchor_y='center')
    def __init__(self):
        self.window.set_fullscreen(True)
        self.window_x = self.window.width
        self.window_y = self.window.height
        #self.window.set_caption('WMP alpha version')

        @self.window.event
        def on_draw():
            self.window.clear()
            self.label.draw()

        pyglet.app.run()


