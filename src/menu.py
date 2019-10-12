import pyglet
from tkinter import filedialog
from tkinter import Tk
from pathlib import Path
import threading
from button import Button
from preview import Preview


def LoadImagesPaths(path, image_paths, loaded):
    loaded[1] = True
    for filename in Path(path).glob("**/*.jpg"):
        image_paths.append(filename)
    number = len(image_paths)
    print("number of images loaded: ", number)
    loaded[0] = True
    loaded[1] = False
    loaded[2] = number

def ExitCallback():
    exit()
    
def OpenFolderCallback():
    root = Tk()
    root.filename = filedialog.askdirectory(initialdir = "/")
    return root.filename  

class Menu:
    root = None
    is_imagesloaded = [False, False, None]
   
    text = None
    label = pyglet.text.Label("Images Loaded:",font_name='Times New Roman',font_size=12,x=70, y=640,anchor_x='center', anchor_y='center')
    image_paths = []
    buttons = []
    preview = None

    loader_idle = pyglet.image.load_animation("./resources/images/loading.gif")
    loader_green = pyglet.image.load_animation("./resources/images/loading2.gif")
    bin = pyglet.image.atlas.TextureBin()
    bin_green = pyglet.image.atlas.TextureBin()
    loader_idle.add_to_texture_bin(bin)
    loader_green.add_to_texture_bin(bin)
    loader_sprite = pyglet.sprite.Sprite(img=loader_idle)
    loader_sprite_green = pyglet.sprite.Sprite(img=loader_green)

    folder_button_image = pyglet.image.load('./resources/images/button_orange.png') 
    folder_button = Button(70, 170, 125, 100, folder_button_image, "Open folder")
    exit_button = Button(70, 50, 125, 100, folder_button_image, "Exit")
    
    def __init__(self):
        self.loader_sprite.scale = 0.2
        self.loader_sprite.x = 0
        self.loader_sprite.y = 700

        self.loader_sprite_green.scale = 0.2
        self.loader_sprite_green.x = 0
        self.loader_sprite_green.y = 700
        
        self.exit_button.SetMouseCallback(ExitCallback)
        self.folder_button.SetMouseCallback(OpenFolderCallback)

        self.buttons.append(self.folder_button)
        self.buttons.append(self.exit_button)

    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,[0, 1, 2, 0, 2, 3],('v2i', (0, 0,140, 0, 140, 1080,0, 1080)),('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)))
        for i in self.buttons:
            i.render()

        if self.is_imagesloaded[1]:
            self.loader_sprite_green.draw()
        else:
            self.loader_sprite.draw()
        if self.text is not None:
            self.text.draw()
            self.label.draw()
        
        if self.preview is not None:
            self.preview.render()

    def update(self, dt):
        for i in self.buttons:
            i.update(dt)
            if i.path is not None:
                self.root = i.path
                i.path = None
                self.LoadImagePaths()
        
        if self.is_imagesloaded[2] is not None and self.text is None:
            self.LoadImagesLabel()
            self.preview = Preview(self.image_paths, 280, 100)

        if self.preview is not None:
            self.preview.update(dt)

    def CheckClicks(self, xc, yc):
        for i in self.buttons:
            i.clicked(xc, yc)

    def CheckFocus(self, xc, yc):
        for i in self.buttons:
            i.focused(xc, yc)
        if self.preview is not None:
            self.preview.onFocus(xc,yc)

    def LoadImagePaths(self):
        x = threading.Thread(target=LoadImagesPaths, args=(self.root,self.image_paths,self.is_imagesloaded,))
        x.start()

    def LoadImagesLabel(self):
        self.text = pyglet.text.Label(str(self.is_imagesloaded[2]),font_name='Times New Roman',font_size=12,x=70, y=620,anchor_x='center', anchor_y='center')


    