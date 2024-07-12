import cv2
cam = cv2.VideoCapture(0) #captures video, only the first one
while True: #forever
    _, frame = cam.read()
    cv2.imshow('Eye Control Mouse', frame) #show some image called eye control mouse
    cv2.waitKey(1) #wait for a key if i press a key, wait for 1 key