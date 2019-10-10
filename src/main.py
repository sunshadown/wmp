import cv2
import pyglet
from application import Application

def main():
    print("Using opencv version: " + cv2.__version__)
    pyglet.options['search_local_libs'] = True
    
    instance = Application()
    instance.CreateWindow()


if __name__ == "__main__":
    main()
