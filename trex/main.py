import cv2
import pyautogui
from skimage.measure import label
from mss import mss
import time 
import webbrowser
import numpy as np
#1095

webbrowser.open('https://chromedino.com')
time.sleep(5)

with mss() as sct:
    sct.shot() 
    first_shot = cv2.imread("monitor-1.png")
    pyautogui.press("space") 
    sct.shot()
    second_shot = cv2.imread("monitor-1.png")
    time.sleep(2)
    sct.shot()
    third_shot = cv2.imread("monitor-1.png")

first_shot = cv2.cvtColor(first_shot, cv2.COLOR_BGR2GRAY)   
first_shot[first_shot!=83]=0
first_shot[first_shot>0]=1


# _, first_shot = cv2.threshold(first_shot,  100, 255,   cv2.THRESH_BINARY_INV)


second_shot = cv2.cvtColor(second_shot, cv2.COLOR_BGR2GRAY)  
second_shot[second_shot!=83]=0 
second_shot[second_shot > 0]=1
# _, second_shot = cv2.threshold(second_shot,  100, 255,   cv2.THRESH_BINARY_INV)


third_shot = cv2.cvtColor(third_shot, cv2.COLOR_BGR2GRAY) 
third_shot[third_shot!=83]=0
third_shot[third_shot>1]=1  
# _, third_shot = cv2.threshold(third_shot,  100, 255,   cv2.THRESH_BINARY_INV)


first_shot = np.copy(first_shot)
second_shot = np.copy(second_shot)
third_shot = np.copy(third_shot)

final_shot = np.bitwise_xor(first_shot, second_shot)
first_shot = np.bitwise_xor(first_shot, third_shot)
final_shot = np.bitwise_xor(final_shot, first_shot)

ay, ax = np.where(final_shot)
# minx=np.min(ax)
# miny=np.min(ay)
# width=np.max(ax)-minx
# hight=np.max(ay)-miny
# print(minx, miny, width, hight)


cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

            
with mss() as sct:
    minx=np.min(ax)
    miny=np.min(ay)
    width=np.max(ax)-minx
    hight=np.max(ay)-miny
    miny = int(miny+hight/1.6)
    hight = int(hight//3.4)
    print(minx, miny, width, hight)

    monitor = {"top": miny, "left": minx, "width": width, "height": hight}
    poin_trigger=int(width//5) 
    poin_trigger1=int(width//5) 
    jump = poin_trigger=int(width//5) 
    jumps = 0
    first_time = time.time()
    p=0
    while "Screen capturing":                              
        last_time = time.time()

        img = np.array(sct.grab(monitor))
        binImage = np.zeros(img.shape[:-1])
        binImage[np.all(img==(83,83,83,0), axis=2)]=1
        cv2.imshow("Image", binImage)
        if binImage[:, poin_trigger].sum()>0  or binImage[:, poin_trigger1].sum()>0 :
            pyautogui.press("space")
            jump = 1
            p+=0.05
            poin_trigger=int(poin_trigger+p)
        elif jump == 1 and binImage[30:36, 0:width//16].sum() > 9 and binImage[36, 0:width//16].sum() < 30 :
            pyautogui.press("down")
            jump = 0
        
        

        
        

        

        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    
cv2.destroyAllWindows()

    




# while True:
#     with mss() as sct:
#         sct.shot()   
#         pyautogui.press("space")          