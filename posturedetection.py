import cv2
import mediapipe as mp
print(mp.__version__)
print(dir(mp))
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils #used to draw the landmarks
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands = 2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    
    #img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(frame_rgb)
    resulthand = hands.process(frame_rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    if results.hand_landmarks:
        mp_draw.draw_landmarks(frame, results.hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Pose Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27: #esc key
        break

cap.release()
cv2.destroyAllWindows()