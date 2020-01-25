import cv2
import numpy as np
import matplotlib.pyplot as plt

def colorDef(typ):
    if typ == 'text':
        return (255,0,0)
    if typ == 'stamp':
        return (0,255,0)
    if typ == 'logo':
        return (0,0,255)
    if typ == 'foto':
        return (255,255,0)
    if typ == 'table':
        return (255,0,255)
    if typ == 'signature':
        return (0,255,255)
    return (0,0,0)
# w name podajesz numer zdjęcia
# w wyświetlonym oknie zanaczasz obszar który cię interesuje po czym wciskasz enter albo spacje, jak nie chcesz już zanaczać to c
# następnie w konsoli wpisujesz co chcesz aby było zanaczone w  obszarze
# następnie musisz podać (2,3) wpisujesz 2 gdy na zaznaczonym obszarze masz tylko tło i to co chcesz zanaczyć, jak coś jeszcze jest to dajesz 3
# jak wybrałeś 3 to wyświeli ci się obraz z zaznaczonymi obszarami w kolorach r g i b te kolory pokazują co jest kolorowane 
# (dalsza część przy wyborze 3)jak wyłączysz to okno z zanaczonymi obszarami to w konsoli musisz podać jaki kolor cię interesuje z tego obszaru (r,g lub b)
# powtarzasz aż wszystko zanczysz
# wpisująć exit obrazek jest zapisywany i program się kończy
# jak popełnisz błąd to nie da się go cofnąć xD trzeba wtedy od nowa zaczynać xD
# co nie wyjdzie trzeba ręcznie
name = '87e'
#77, 80, 83, 86 zdjecie zle zrobione
image = cv2.imread("C:/GitRepos/wmp/doc_seg/dokumenty/test/"+name+".jpg")
inp = 'start'
while inp != 'exit':
    roi = cv2.selectROI(image,False)  
    print("Podaj typ(text,stamp,logo,foto,table,signature,exit):")
    inp = input()
    color = colorDef(inp)
    if color != (0,0,0):
        print("Podaj ilość klastrów (2,3):")
        k = int(input())
        img = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        pixel_values = img.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()
        if k == 3:
            background = centers.copy()
            centers[0] = (255,0,0)
            centers[1] = (0,255,0)
            centers[2] = (0,0,255)
            segmented_image = centers[labels.flatten()]
            segmented_image = segmented_image.reshape(img.shape)
            plt.imshow(segmented_image)
            plt.show()
            print("Jaki kolor odpowiada "+inp+" (r,g,b)?")
            inp = input()
            if inp == 'r':
                background[0] = color
            elif inp == 'g':
                background[1] = color
            elif inp == 'b':
                background[2] = color
            segmented_image = background[labels.flatten()]
            segmented_image = segmented_image.reshape(img.shape)
            if inp != 'r' and inp != 'g' and inp != 'b':
                segmented_image = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        if k == 2:         
            background = centers[0].copy()
            centers[0] = color          
            segmented_image = centers[labels.flatten()]
            segmented_image = segmented_image.reshape(img.shape)
            if segmented_image[0,0,0]==color[0] and segmented_image[0,0,1]==color[1] and segmented_image[0,0,2]==color[2]:
                centers[0] = background
                centers[1] = color
                segmented_image = centers[labels.flatten()]
                segmented_image = segmented_image.reshape(img.shape)
        if k != 2 and k !=3:
            segmented_image = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] = segmented_image

cv2.destroyAllWindows()
cv2.imwrite("C:/GitRepos/wmp/doc_seg/dokumenty/test/"+name+"ref.jpg",image)
