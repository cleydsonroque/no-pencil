import numpy as np
import cv2
from matplotlib import pyplot as plt

def showIMG(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    obj_img = cv2.imread('img.jpg')
    # cut_img = obj_img[1200:1200 + 100, 800:800 + 100]
    height, width, color_channels = obj_img.shape

    for y in range(0, height):
        print(f'{y} de {height}')
        for x in range(0, width):
            pixel = obj_img[y][x]
            for rgb in range(67, 205):
                if pixel[2] == rgb: 
                    obj_img.itemset((y,x,0),255)
                    obj_img.itemset((y,x,1),255)
                    obj_img.itemset((y,x,2),255)
    cv2.imwrite("img_np_1.jpg", obj_img)
    showIMG(obj_img)

main()