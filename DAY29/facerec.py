import cv2

haar_file="haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar_file)
cam = cv2.VideoCapture(0)
(width, height) = (130, 100)
while True:
    (_, img) = cam.read()
    img=cv2.flip(img,1)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = grayImg[y: y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
    cv2.imshow('OPENCV', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("e"):
        break

cam.release()
cv2.destroyAllWindows()
