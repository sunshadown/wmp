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
from compareResult import maxPixels
import os

files = [f for f in os.listdir("doc_seg/dokumenty/test_ref/") if os.path.isfile(os.path.join("doc_seg/dokumenty/test_ref/", f))]
files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

options = {"model": "doc_seg/cfg/tiny-yolo-voc-6c.cfg","load": -1, "gpu": 0.8, "labels": "doc_seg/dok_lab.txt",'backup':'ckpt/',"threshold": 0.5}

tfnet = TFNet(options)
tfnet.load_from_ckpt()

score = []
for f in range(0,len(files),2):
    imgcv = cv2.imread("doc_seg/dokumenty/test_ref/"+files[f])
    ref = cv2.imread("doc_seg/dokumenty/test_ref/"+files[f+1])
    result = tfnet.return_predict(imgcv)

    allPix = maxPixels(ref)
    detectPIx = 0
    for i in range(len(result)):
        temp = 0
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
    
    score.append(round((100*detectPIx)/allPix,2))
    cv2.imwrite("doc_seg/dokumenty/classifier/("+str(round((100*detectPIx)/allPix,2))+")"+files[f],imgcv)
    print('Classified: '+str(f/2+1)+'/'+str(len(files)/2),end='\r')
print('Result for all image is: '+str(round(np.sum(score)/len(score),2))+'%')