import cv2
import numpy as np
from skimage.measure import label, regionprops
import matplotlib.pyplot as plt
from pathlib import Path


vid_capture = cv2.VideoCapture("pictures.avi")
if (vid_capture.isOpened()==False):
    print("Ошибка чтения файла")
else:
    fps = vid_capture.get(5)
    print('Фреймов в секунду: ', fps,'FPS')
    frame_count = vid_capture.get(7)

my_pictures_count = 0
path = Path(".")/ "result8"
path.mkdir(exist_ok=True)
while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret==True:
        gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        th, im_th = cv2.threshold(gr,  180, 255,   cv2.THRESH_BINARY)
        im_th[im_th==0]=1
        im_th[im_th==255]=0
        labled = label(im_th)
        
        if np.max(labled)==3:
            regions = regionprops(labled)
            region = regions[2]
            ny, nx = (region.local_centroid[0]/region.image.shape[0],
            region.local_centroid[1]/region.image.shape[1])
            if abs(nx-ny)<0.01:
                my_pictures_count+=1
                plt.clf()
                plt.imshow(frame)
                plt.tight_layout()
                plt.savefig(path  / f"{my_pictures_count}.png")
    else:
        break
            
            
print(my_pictures_count)

            

