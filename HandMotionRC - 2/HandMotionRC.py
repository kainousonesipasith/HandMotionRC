import cv2
import mediapipe as mp

# Initialize MediaPipe hands and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Open video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cannot access camera")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(frame_rgb)

    # Initialize output values
    go_value = None
    left_value = 0  # Default value for left hand
    right_value = 0  # Default value for right hand

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Determine the wrist position to identify left or right hand
            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x

            if wrist_x < 0.5:  # If the hand is on the left side
                # Check for left hand actions (only go value)
                if (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <
                        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y):
                    # Fist
                    go_value = 0  # Fist
                else:
                    # Open hand
                    go_value = 1  # Open hand
            else:  # If the hand is on the right side
                # Check for right hand actions
                thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
                index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y

                # Two fingers up action (thumb and index finger up)
                if (index_tip_y < index_mcp_y) and (thumb_tip_y < thumb_mcp_y):
                    right_value = 0  # Right hand (two fingers up)
                    left_value = 1  # Two fingers up
                # Open hand action
                elif thumb_tip_y < thumb_mcp_y:
                    right_value = 1  # Open hand
                    left_value = 0
                else:
                    right_value = 0  # Fist
                    left_value = 0

    # Display values for left hand (only go value) and right hand
    if go_value is not None:
        display_text = f"go: {go_value}, left: {left_value}, right: {right_value}"
    else:
        display_text = f"go: {1 if left_value == 1 else 0}, left: {left_value}, right: {right_value}"

    # Show the display text on the frame
    cv2.putText(frame, display_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow("Hand Detection", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

