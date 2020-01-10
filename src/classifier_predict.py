from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from darkflow.net.build import TFNet
import cv2



options = {"model": "doc_seg/cfg/tiny-yolo-voc-6c.cfg", "gpu": 0.8,"load": -1, "labels": "doc_seg/dok_lab.txt",'threshold': 0.04}

tfnet = TFNet(options)

imgcv = cv2.imread("./doc_seg/dokumenty/learn/12.jpg")
result = tfnet.return_predict(imgcv)
print(result)