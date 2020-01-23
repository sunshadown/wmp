import cv2
import numpy as np
import math

def segmentation(img,top,bot,color,typ):
    crop,edged,x1,x2,y1,y2 = resizeROI(img,top,bot,5)

    crop = img[y1:y2,x1:x2]
    pixel_values = crop.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
  
    _, labels, (centers) = cv2.kmeans(pixel_values, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    background = centers[0].copy()
    tresh = calcDiff(centers[1])
    centers[0] = color
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(crop.shape)
    if segmented_image[0,0,0]!=color[0] and segmented_image[0,0,1]!=color[1] and segmented_image[0,0,2]!=color[2]:
        background = centers[1].copy()
        tresh = calcDiff(centers[0])

    k = 3    
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)

    idx = findBack(background,centers) 
    for i in range(k):
        if i != idx:
            if typ != 'text':
                if centers[i,0]>100 or centers[i,1]>100 or centers[i,2]>100:
                    centers[i] = color 
            else:
                if calcDiff(centers[i])<=tresh:
                    centers[i] = color

    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(crop.shape) 

    img[y1:y2,x1:x2] = segmented_image
    return img

def findBack(back,center):
    back = np.float32(back)
    center = np.float32(center)
    length = []
    for i in range(len(center)):
        length.append(math.sqrt(pow(back[0]-center[i,0],2)+pow(back[1]-center[i,1],2)+pow(back[2]-center[i,2],2)))
    return length.index(min(length))

def calcDiff(num):
    num = np.float32(num)
    return abs(num[0]-num[1])+abs(num[0]-num[2])+abs(num[1]-num[2])

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
