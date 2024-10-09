import cv2
import mediapipe as mp

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to make it mirror-like
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    left_wheel = 0  # Control value for left wheel
    right_wheel = 0  # Control value for right wheel

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Check if it's left or right hand based on handedness
            if results.multi_handedness[idx].classification[0].label == 'Left':
                # Left hand actions: control left wheel
                thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                pinky = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                # Check for actions based on finger positions
                if index_finger < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and \
                        middle_finger < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and \
                        ring_finger < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and \
                        pinky < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:  # 1 Finger up (Index)
                    left_wheel = 1  # Left wheel goes backward
                elif all(finger > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y for finger in [thumb, index_finger, middle_finger, ring_finger, pinky]):  # All fingers down (fist)
                    left_wheel = 0  # Left wheel stops
                else:  # Open hand (fingers apart)
                    left_wheel = -1  # Left wheel goes forward

            elif results.multi_handedness[idx].classification[0].label == 'Right':
                # Right hand actions: control right wheel
                thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                pinky = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                # Check for actions based on finger positions
                if index_finger < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and \
                        middle_finger < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and \
                        ring_finger < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and \
                        pinky < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:  # 1 Finger up (Index)
                    right_wheel = 1  # Right wheel goes backward
                elif all(finger > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y for finger in [thumb, index_finger, middle_finger, ring_finger, pinky]):  # All fingers down (fist)
                    right_wheel = 0  # Right wheel stops
                else:  # Open hand (fingers apart)
                    right_wheel = -1  # Right wheel goes forward

            # Draw the hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the wheel status on the screen
    cv2.putText(frame, f'Left wheel: {left_wheel}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f'Right wheel: {right_wheel}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the video
    cv2.imshow('Hand Motion RC Control', frame)

    # Press 'q' to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
