import cv2

img = cv2.imread('group2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#use haar cascade model to detect faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(gray)

print("Found {0} Faces!".format(len(faces)))

counter = 0

#find the face
for(x, y, w, h) in faces:

    #uncomment for demo purposes
    #cv2.rectangle(img, (x, y), (x+w, y+h),
    #            (255, 0, 0), 2)
    
    faces = img[y:y + h, x:x + w]    

    #cv2.imshow("face", faces)
    fileName = './faces/faces' + str(counter) + '.jpg'
    cv2.imwrite(fileName, faces)
    counter += 1

cv2.imshow('img', img)
cv2.waitKey()

