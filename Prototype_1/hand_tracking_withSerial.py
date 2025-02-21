#In this part we will communicate with the esp 32
import cv2
import mediapipe as mp
import serial
import time

#setting up serian communication with the esp32
try:
    esp_serial = serial.Serial("COM8",115200,timeout = 1)
    time.sleep(2)
    print("---- SERIAL COMMUNICATION ESTABLISHED SUCCESSFULLY ----")
except:
    print("---- UNABLE TO COMMUNICATE TO ESP32 ----")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence = 0.7 , min_tracking_confidence = 0.7)
mp_draw = mp.solutions.drawing_utils


#opening the video cam and getting dimensions
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    

    #now for performing natural movements we need to flip the fram 
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    #initializing movement command
    movement_cmd = "S" #default : STOP
    frame_center = width // 2
    
    #Processing detected hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            cx = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x*width)
            cy = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y*height)
            
            
            #converting hand location to command 
            if cx < frame_center - 100:
                movement_cmd = "L" #left
            elif cx > frame_center + 100:
                movement_cmd = "R" #right
            elif cy < height // 3:
                movement_cmd = "F"
            elif cy > (2*height) //3:
                movement_cmd = "B"
                
                
            #writting command to Serial
            if esp_serial.is_open:
                esp_serial.write((movement_cmd + "\n").encode())
                
            #drawing Landmarks
            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            #displaying the command on the frame
            cv2.putText(frame , f"MOVE : {movement_cmd}",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Camera test",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
esp_serial.close()
print("---- SERIAL COMMUNICATION CLOSED ----")




