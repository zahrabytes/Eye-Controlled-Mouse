import cv2
import mediapipe as mp #shortname mp

face_mesh = mp.solutions.face_mesh.FaceMesh() #capture a face mesh called face_mesh
cam = cv2.VideoCapture(0) #captures video, only the first one
while True: #forever
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert color of frame bgr to rgb
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks #landmarks on face
    #print(landmark_points) #show if face is detected or not
    frame_h, frame_w, _ = frame.shape #shape of video 
    if landmark_points:
        landmarks = landmark_points[0].landmark #only one face
        for landmark in landmarks:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y), 3, (0, 255, 0))
            print(x,y)
    cv2.imshow('Eye Control Mouse', frame) #show some image called eye control mouse
    cv2.waitKey(1) #wait for a key if i press a key, wait for 1 key
