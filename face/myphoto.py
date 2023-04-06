import cv2
x=cv2.VideoCapture(0)
#y,z=x.read()
def face(z):
    face_data= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        i=0
        y,z=x.read()
        gs=cv2.cvtColor(z,cv2.COLOR_BGR2GRAY)
        fcc=face_data.detectMultiScale(gs)
        for (i,j,k,l) in face_coordinates:
                cv2.rectangle(frame , (i , j) , (i+k , j+l) , (255 , 0 , 0) , 2) #RGB
                i=i+1
        cv2.imshow('Frontal_Face',z)
        key = cv2.waitKey(1)
        if key == 81 or key == 113:
                break
x.release()
    
'''
cv2.imshow("Shagun",z)
cv2.imwrite("Utsa.png",z)
cv2.destroyallwindows()
'''
