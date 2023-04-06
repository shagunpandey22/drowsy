
import cv2
'''
def face(x):   #face_daetection
     face_data= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
     while True:
         i=0
         y,z=x.read()
         gs=cv2.cvtColor(z,cv2.COLOR_BGR2GRAY)
         fcc=face_data.detectMultiScale(gs)
         for (i,j,k,l) in fcc:
                cv2.rectangle(z , (i , j) , (i+k , j+l) , (255 , 0 , 0) , 2) #RGB
                i=i+1
         cv2.imshow('Frontal_Face',z)
         cv2.imwrite("Save_img.png",z) #save the image in the folder where your program is stored
         f= cv2.waitKey(1)
         if f == 90 or f ==120:
                break
     return z'''
def eye(x):    #eye_detection
    eye_data=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    t = 0
    while True:
        i=0
        
        y,z=x.read()
        gs=cv2.cvtColor(z,cv2.COLOR_BGR2GRAY)
        ecc=eye_data.detectMultiScale(gs)
    
        for (i,j,k,l) in ecc:
                cv2.rectangle(z , (i , j) , (i+k , j+l) , (0 , 255 , 0) , 2) #RGB
                i=i+1
                t=1
        
        if t==1:
            cv2.imshow('EYE',z[i:i+k, j:j+l])
        else:
            cv2.imshow('EYE',z)
            
         #save the image in the folder where your program is stored
        f= cv2.waitKey(1) 
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) 
        closed = cv2.morphologyEx(z, cv2.MORPH_CLOSE, kernel) 
       # cv2.imshow("Closed", closed)
        #(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        #for c in cnts: 
         #       peri = cv2.arcLength(c, True) 
          #      approx = cv2.approxPolyDP(c, 0.02 * peri, True) 
           #     cv2.drawContours(z, [approx], -1, (0, 255, 0), 2) 
        cv2.imshow("Output",z)
        cv2.imwrite("Save_img.png",z)
        cv2.waitKey(0)

        if f == 90 or f ==120:
                break
    return z


'''
def smile(x):
    smile_data=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    while True:
        i=0
        y,z=x.read()
        gs=cv2.cvtColor(z,cv2.COLOR_BGR2GRAY)
        scc=smile_data.detectMultiScale(gs)
        for (i,j,k,l) in scc:
                cv2.rectangle(z , (i , j) , (i+k , j+l) , (0 , 0 , 255) , 2) #RGB
                i=i+1
        cv2.imshow('SMILE_PLEASE',z)
        cv2.imwrite("Save_img.png",z) #save the image in the folder where your program is stored
        f= cv2.waitKey(1)
        if f == 90 or f ==120:
                break
    return z
 '''   
#input of camera number
#print("Enter the Camera Number")
#cam=int(input())  #pass the camera number in the VideoCapture
#x=cv2.VideoCapture(cam)
#The camera of laptop value is zero so taken it as default only
x=cv2.VideoCapture(0)
#eye_detection
res=eye(x)
cv2.imshow(res)
cv2.imwrite("Utsa.png",res)
#face_detection

#ans=face(x)
#cv2.imshow(ans)
#y,z=x.read()
#smile_detection

#s=smile(x)
#cv2.imshow(s)

x.release()
    

#cv2.imshow("Shagun",z)
#cv2.imwrite("Utsa.png",res)
cv2.destroyallwindows() 



