from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from darkflow.net.build import TFNet
import cv2
import json
import cv2
from stamp_segmentation import segmentation
from object_list import color_list
from compareResult import maxPixels


options = {"model": "doc_seg/cfg/tiny-yolo-voc-6c.cfg","load": -1, "gpu": 0.8, "labels": "doc_seg/dok_lab.txt",'backup':'ckpt/',"threshold": 0.5}

name = '2'
tfnet = TFNet(options)
tfnet.load_from_ckpt()
imgcv = cv2.imread("doc_seg/dokumenty/test/"+name+".jpg")
ref = cv2.imread("doc_seg/dokumenty/test/"+name+"ref.jpg")
result = tfnet.return_predict(imgcv)
print(result)

allPix = maxPixels(ref)
detectPIx = 0
for i in range(len(result)):
    data = result[i]
    top = data['topleft']
    bot = data['bottomright']
    text = data['label']
    if text == 'text':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(255,0,0),text)
    if text == 'stamp':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(0,255,0),text)
    if text == 'logo':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(0,0,255),text)
    if text == 'foto':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(255,255,0),text)
    if text == 'table':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(255,0,255),text)
    if text == 'signature':
        imgcv,temp = segmentation(imgcv,ref,top,bot,(0,255,255),text)
    detectPIx = detectPIx +temp

print('Detected: '+str(round((100*detectPIx)/allPix,2))+'%'+' of all pixels')

shape = imgcv.shape
shape = list(shape)
if shape[0]>1000 or shape[1]>1000:
    shape[1] = int(shape[1]*0.5)
    shape[0] = int(shape[0]*0.5)

cv2.imshow('Detected',cv2.resize(imgcv,(shape[1],shape[0])))
cv2.imshow('Reference',cv2.resize(ref,(shape[1],shape[0])))
cv2.imshow('Color object',color_list())
cv2.waitKey(0)
cv2.destroyAllWindows()

