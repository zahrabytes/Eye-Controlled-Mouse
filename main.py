import cv2
import mediapipe as mp #shortname mp
import pyautogui
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) #capture a face mesh called face_mesh, refine the landmarks on face
screen_w, screen_h = pyautogui.size()
cam = cv2.VideoCapture(0) #captures video, only the first one
while True: #forever
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert color of frame bgr to rgb
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks #landmarks on face
    #print(landmark_points) #show if face is detected or not
    frame_h, frame_w, _ = frame.shape #shape of video 
    if landmark_points:
        landmarks = landmark_points[0].landmark #only one face
        for id, landmark in enumerate(landmarks[474:478]): #these four different landmarks are one of your eye, enumarate will give you the id or index and second will be landmark
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y), 3, (0, 255, 0)) #mark right eye by circles
            if id == 1:
                screen_x = screen_w / frame_w * x #scale the cursor coordinates
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y) #move the cursor
        left = [landmarks[145], landmarks[159]] #top and bottom of eye
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y), 3, (0, 255, 255)) #mark left eye by circles
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click() #actual click
            pyautogui.sleep(1) #sleep after click
    cv2.imshow('Eye Control Mouse', frame) #show some image called eye control mouse
    cv2.waitKey(1) #wait for a key if i press a key, wait for 1 key
