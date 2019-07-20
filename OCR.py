import pytesseract
import numpy as np
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    
    img=cv2.imread('testocr.png')
    img=cv2.resize(img,None,fx=0.5,fy=0.5)
    kernel=np.ones((2,2),dtype=np.uint8)
    img=cv2.erode(img,kernel,iterations=1)
    img=cv2.dilate(img,kernel,iterations=1)
    read=pytesseract.image_to_string(img)
    #read=pytesseract.image_to_boxes(img)
    #read=pytesseract.image_ro_data(img)
    print(read)

except Exception as e:
    print("No image found")
    print(e)
    
