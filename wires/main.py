from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np


im1 = np.load('lect 1/wires6.npy.txt')
p=1
im1 = label(im1)


for i in range(1, np.max(im1)+1):
    sub = im1 == p
    sub = binary_erosion(sub)
    sub = label(sub)
    max_broke = np.max(sub)
    if max_broke==0:
        print("Провод", p, "полностью не исправет")
        p+=1
        continue
    if max_broke==1:
        print("Провод", p, "полностью  исправет")
        p+=1
        continue
    print(f"Провод {p} порван на {np.max(sub)}")
    p+=1
        



# im1 = label(im1)
# countp = np.max(im1)
# print(countp)
# im1 = binary_erosion(im1)
# im1 = label(im1)

# plt.imshow(im1)
# plt.show()
