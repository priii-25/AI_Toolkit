import cv2
import numpy as np
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera == True:
    success, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))

    cv2.imshow('Result', frame)
    cv2.waitKey(1
