from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from darkflow.net.build import TFNet
import cv2
import json
import cv2

options = {"model": "doc_seg/cfg/tiny-yolo-voc-6c.cfg","load": -1, "gpu": 0.8, "labels": "doc_seg/dok_lab.txt",'backup':'ckpt/',"threshold": 0.1}

tfnet = TFNet(options)
tfnet.load_from_ckpt()
imgcv = cv2.imread("doc_seg/dokumenty/learn/38.jpg")
result = tfnet.return_predict(imgcv)
print(result)


for i in range(len(result)):
    data = result[i]
    top = data['topleft']
    bot = data['bottomright']
    text = data['label']
    if text == 'text':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (255,0,0), 2)
    if text == 'stamp':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (0,255,0), 2)
    if text == 'logo':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (0,0,255), 2)
    if text == 'foto':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (255,255,0), 2)
    if text == 'table':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (255,0,255), 2)
    if text == 'signature':
        imgcv = cv2.rectangle(imgcv, (top['x'],top['y']),(bot['x'],bot['y']), (0,255,255), 2)

cv2.namedWindow("top",cv2.WINDOW_FREERATIO)
cv2.imshow('top',imgcv)
cv2.waitKey(0)
cv2.destroyAllWindows()

