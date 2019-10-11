import pyglet
from pyglet.window import key
from button import Button
class Window:
    window = pyglet.window.Window(caption='WMP alpha version')
    window_x = None
    window_y = None
    background = pyglet.image.load('./resources/images/background.jpg')
    button_image = pyglet.image.load('./resources/images/stypendium.png') 
    button = Button(0, 0, 100, 100, button_image)
    buttons = []
    label = pyglet.text.Label('WMP alpha',
                          font_name='Times New Roman',
                          font_size=36,
                          x=200, y=800,
                          anchor_x='center', anchor_y='center')
    def __init__(self):
        self.window.set_fullscreen(True)
        self.window_x = self.window.width
        self.window_y = self.window.height

        def update(dt):
            pass

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background.blit(0,0)
            self.label.draw()
            self.button.render()
        
        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.ESCAPE:
                exit()
        pyglet.clock.schedule_interval(update, 1/60.)
        pyglet.app.run()



