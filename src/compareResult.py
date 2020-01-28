import cv2
import numpy as np
import matplotlib.pyplot as plt


def compareResult(img,imgRef,roi,typ):
    h_low = h_val(typ)
    imgRef = imgRef[roi[2]:roi[3],roi[0]:roi[1]]
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
    imgRef_hsv = cv2.cvtColor(imgRef,cv2.COLOR_BGR2HSV)
    img_hsv = cv2.inRange(img_hsv,(h_low,125,125),(h_low+10,255,255))
    imgRef_hsv = cv2.inRange(imgRef_hsv,(h_low,125,125),(h_low+10,255,255))
    img_hsv=img_hsv/255 
    imgRef_hsv=imgRef_hsv/255
    sum_img = np.sum(img_hsv)  
    sum_ref = np.sum(imgRef_hsv)
    if sum_ref == 0:
        return 0.0,0
    else:
        pixel = sum_ref
        percent = (100*sum_img)/sum_ref
        if percent > 200 or percent < 80:
            pixel = 0
        elif percent >= 80 and percent <=100:
            pixel = sum_img
        return percent,pixel 

def maxPixels(img):
    typ = ['text','stamp','logo','foto','table','signature']
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    sum_img = 0
    for i in typ:
        h_low = h_val(i)
        img_temp = cv2.inRange(img_hsv,(h_low,125,125),(h_low+10,255,255))
        img_temp=img_temp/255 
        temp = np.sum(img_temp)
        sum_img = sum_img+temp
    return sum_img

def h_val(typ):
    if typ == 'text':
        return 115
    if typ == 'stamp':
        return 55
    if typ == 'logo':
        return 0
    if typ == 'foto':
        return 85
    if typ == 'table':
        return 145
    if typ == 'signature':
        return 25
