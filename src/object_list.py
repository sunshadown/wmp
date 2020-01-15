import cv2
import numpy as np

def color_list():
    img = np.zeros((240,400,3))
    img = cv2.rectangle(img,(0,0),(200,40),(255,0,0),cv2.FILLED)
    img = cv2.putText(img,'text',(210,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    img = cv2.rectangle(img,(0,40),(200,80),(0,255,0),cv2.FILLED)
    img = cv2.putText(img,'stamp',(210,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    img = cv2.rectangle(img,(0,80),(200,120),(0,0,255),cv2.FILLED)
    img = cv2.putText(img,'logo',(210,110),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    img = cv2.rectangle(img,(0,120),(200,160),(255,255,0),cv2.FILLED)
    img = cv2.putText(img,'foto',(210,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    img = cv2.rectangle(img,(0,160),(200,200),(255,0,255),cv2.FILLED)
    img = cv2.putText(img,'table',(210,190),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    img = cv2.rectangle(img,(0,200),(200,240),(0,255,255),cv2.FILLED)
    img = cv2.putText(img,'signature',(210,230),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    return img
