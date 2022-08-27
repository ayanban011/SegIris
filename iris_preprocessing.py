# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 10:22:11 2022

@author: Ayan
"""

import cv2
import glob
def process(filename, key):
    img = cv2.imread(filename)
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #hsv_save=cv2.imwrite('D:\\Downloads\\attachments\\image_1_h.png',hsvImage)
    imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    #ycc_save=cv2.imwrite('D:\\Downloads\\attachments\\image_1_y.png',imgYCC)

    gray_h = cv2.cvtColor(hsvImage, cv2.COLOR_BGR2GRAY)
    gray_y = cv2.cvtColor(imgYCC, cv2.COLOR_BGR2GRAY)

    blur1 = cv2.GaussianBlur(gray_h,(5,5),0)
    ret3,th3 = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blur2 = cv2.GaussianBlur(gray_y,(5,5),0)
    ret4,th4 = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    superimposed_img = th4+0.8*th3

    #thresh_s = cv2.imwrite('D:\\Downloads\\attachments\\image_1_y_b.png',th4)

    #s_s = cv2.imwrite('D:\\Downloads\\attachments\\image_1_s.png',superimposed_img)

    final_mask = superimposed_img[54:121,60:172]
    c_s = cv2.imwrite('D:\\Downloads\\attachments\\final_mask{}.jpg'.format(key), final_mask)


for (i,image_file) in enumerate(glob.iglob('D:\\Downloads\\attachments\\*.png')):
    print(image_file)
    process(image_file, i)

