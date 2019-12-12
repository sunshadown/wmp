from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from darkflow.net.build import TFNet
import cv2

print("TensorFlow version: ",tf.__version__)

options = {"model": "cfg/yolov2.cfg", "load": "bin/yolov2.weights","train": "", "dataset": "dokumenty/learn/", "annotation": "dokumenty/learn/" , "labels": "dok_lab.txt"}

tfnet = TFNet(options)

imgcv = cv2.imread("./dokumenty/learn/3.jpg")
result = tfnet.return_predict(imgcv)
print(result)