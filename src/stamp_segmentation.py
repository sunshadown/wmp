import cv2
import numpy as np


def segmentation(img,top,bot,color,typ):
    crop,edged,x1,x2,y1,y2 = resizeROI(img,top,bot,5)
    contours, hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(contours) > 1:
        kernel = np.ones((3,3), np.uint8)
        dilation = cv2.dilate(edged, kernel)
        edged = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
        contours, hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        if len(contours) > 1 and typ != 'text':
            temp = largest_contour_find(contours)
            contours = []
            contours.append(temp)
    cv2.drawContours(crop,contours,-1,color,cv2.FILLED)
    img[y1:y2,x1:x2] = crop
    return img

def resizeROI(img,top,bot,tresh):
    tresh = tresh*255
    yT = top['y']
    yB = bot['y']
    xT = top['x']
    xB = bot['x']
    crop = img[yT:yB,xT:xB]
    gray=cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
    edged=cv2.Canny(gray,30,200)
    yImg = len(img)-1
    xImg = len(img[0])-1
    while 1:
        flag = 0
        y = len(crop)-1
        x = len(crop[0])-1
        if np.sum(edged[0:y,0]) > tresh:
            xT = xT - 1
            flag = 1
            if xT < 0 :
                xT = 0
                flag = 0         
        if np.sum(edged[0:y,x]) > tresh:
            xB = xB + 1
            flag = 1
            if xB > xImg :
                xB = xImg
                flag = 0             
        if np.sum(edged[0,0:x]) > tresh:
            yT = yT - 1
            flag = 1
            if yT < 0 :
                yT = 0
                flag = 0 
        if np.sum(edged[y,0:x]) > tresh:
            yB = yB + 1
            flag = 1
            if yB > yImg :
                yB = yImg
                flag = 0 
        if flag:
            crop = img[yT:yB,xT:xB]
            gray=cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
            edged=cv2.Canny(gray,30,200)
        else:
            break       
    return crop,edged,xT,xB,yT,yB

def largest_contour_find(contours):
    max_area=0
    largest_contour=-1
    for i in range(len(contours)):
        cont=contours[i]
        area=cv2.contourArea(cont)
        if(area>max_area):
            max_area=area
            largest_contour=i
    if(largest_contour==-1):
        return 0
    else:
        l_contour=contours[largest_contour]
        return l_contour
