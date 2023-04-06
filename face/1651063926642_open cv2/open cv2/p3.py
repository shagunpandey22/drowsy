import cv2
import numpy as np
import datetime
vid=cv2.VideoCapture(0)
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
        i=0
        successful_frame_read , frame = vid.read()
        grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
        for (x , y , w , h) in face_coordinates:
                cv2.rectangle(frame , (x , y) , (x+w , y+h) , (255 , 0 , 0) , 2) #RGB
                i=i+1
        cv2.imshow('Name_Your_Frame', frame)
        f= cv2.waitKey(1)
        if f == 90 or f ==120:
                break
vid.release()
