import cv2
from application import Application

def main():
    print("Using opencv version: " + cv2.__version__)
    instance = Application()
    instance.CreateWindow()


if __name__ == "__main__":
    main()
