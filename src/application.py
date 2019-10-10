from window import Window

class Application(object):
    _instance = None  # Keep instance reference 
    windowInstance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def CreateWindow(self):
        windowInstance = Window()