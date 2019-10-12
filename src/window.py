import pyglet
from pyglet.window import key
from pyglet.window import mouse
from menu import Menu

class Window:
    window = pyglet.window.Window(caption='WMP alpha version', resizable = True)
    window_x = None
    window_y = None
    cursor_image = pyglet.image.load("./resources/images/cursor.png")
    cursor = pyglet.window.ImageMouseCursor(cursor_image, 37, 60)
    menu = Menu()
    background = pyglet.image.load('./resources/images/background3.jpg')
    label = pyglet.text.Label('WMP alpha',
                          font_name='Times New Roman',
                          font_size=36,
                          x=270, y=720,
                          anchor_x='center', anchor_y='center')

    def __init__(self):
        #self.window.set_fullscreen(True)
        self.window.set_size(1920,1080)
        self.window_x = self.window.width
        self.window_y = self.window.height
        self.window.set_mouse_cursor(self.cursor)

        def update(dt):
            self.menu.update(dt)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background.blit(0,0)
            self.label.draw()
            self.menu.draw()
        
        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.ESCAPE:
                exit()

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            self.menu.CheckClicks(x,y)

        @self.window.event
        def on_mouse_motion(x, y, dx, dy):
            self.menu.CheckFocus(x,y)

        pyglet.clock.schedule_interval(update, 1/60.)
        pyglet.app.run()



