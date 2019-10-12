import pyglet
from button import Button

def ExitCallback():
    exit()
    print("dupa callback")
    

class Menu:
    buttons = []

    folder_button_image = pyglet.image.load('./resources/images/button_orange.png') 
    folder_button = Button(70, 500, 125, 100, folder_button_image, "Open folder")
    exit_button = Button(70, 300, 125, 100, folder_button_image, "Exit")
    
    def __init__(self):
        self.exit_button.SetMouseCallback(ExitCallback)
        self.buttons.append(self.folder_button)
        self.buttons.append(self.exit_button)

    def draw(self):
        for i in self.buttons:
            i.render()

    def update(self, dt):
        for i in self.buttons:
            i.update(dt)

    def CheckClicks(self, xc, yc):
        for i in self.buttons:
            i.clicked(xc, yc)

    def CheckFocus(self, xc, yc):
        for i in self.buttons:
            i.focused(xc, yc)
        

    