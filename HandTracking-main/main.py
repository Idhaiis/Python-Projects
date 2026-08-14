import cv2
import os
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

images = {
    "ri": cv2.imread("images/ri.jpg"),
    "ri1": cv2.imread("images/ri1.jpeg"),
    "ri2": cv2.imread("images/ri2.jpeg"),
    "ri3": cv2.imread("images/ri3.jpeg"),
    "rirock": cv2.imread("images/rirock.png"),
    "ribus": cv2.imread("images/ribus.png"),
    "rihand": cv2.imread("images/rihand.png"),
    "rinah": cv2.imread("images/rinah.png"),
}

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    current_gesture = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_open = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
            middle_open = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
            ring_open = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
            pinky_open = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y

            index_bent = hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y
            middle_bent = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
            ring_bent = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
            pinky_bent = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y

            index_closed  = hand_landmarks.landmark[8].y  > hand_landmarks.landmark[5].y
            middle_closed = hand_landmarks.landmark[12].y > hand_landmarks.landmark[9].y
            ring_closed   = hand_landmarks.landmark[16].y > hand_landmarks.landmark[13].y
            pinky_closed  = hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y

            thumb_x  = hand_landmarks.landmark[4].x
            index_x  = hand_landmarks.landmark[8].x
            middle_x = hand_landmarks.landmark[12].x

            thumb_between = min(index_x, middle_x) <= thumb_x <= max(index_x, middle_x)
            wrist_near_head = hand_landmarks.landmark[0].y < 0.45

            if index_open and not middle_open and not ring_open and not pinky_open:
                current_gesture = "ri1"
            elif index_open and middle_open and not ring_open and not pinky_open:
                current_gesture = "ri2"
            elif index_open and middle_open and ring_open and not pinky_open:
                current_gesture = "ri3"
            elif index_open and not middle_open and not ring_open and pinky_open:
                current_gesture = "rirock"
            elif index_bent and middle_bent and ring_bent and pinky_bent:
                current_gesture = "ribus"
            elif index_open and middle_open and ring_open and pinky_open:
               current_gesture = "rihand"
            elif index_closed and middle_closed and ring_closed and pinky_closed and thumb_between:
                current_gesture = "rinah"

    if current_gesture in images and images[current_gesture] is not None:
        overlay = cv2.resize(images[current_gesture], (200, 200))
        h, w, _ = overlay.shape
        frame[10:10+h, 10:10+w] = overlay
    else:
        overlay = cv2.resize(images["ri"], (200, 200))
        h, w, _ = overlay.shape
        frame[10:10+h, 10:10+w] = overlay

    cv2.imshow("Recep İvedik OL", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()