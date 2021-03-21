import cv2

cam = cv2.VideoCapture(1)
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('SEC CAm', frame)
