from window import Window
from musicplayer import MusicPlayer

class Application(object):
    _instance = None  # Keep instance reference 
    windowInstance = None
    music = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def CreateWindow(self):
        music = MusicPlayer()
        music.player.play()
        windowInstance = Window()