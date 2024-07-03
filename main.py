import cv2
import mediapipe as mp
import pyautogui as pyg

#Variables
x1 = y1 = x2 = y2 = 0

# Initialize the webcam
webcam = cv2.VideoCapture(0)

# Initialize the MediaPipe Hands and drawing utils
my_hands = mp.solutions.hands.Hands()
draw_utils = mp.solutions.drawing_utils

while True:
    success, image = webcam.read()
    if not success:
        print("Ignoring empty Camera Frame.")
        continue

    # Flip the image horizontally
    image = cv2.flip(image, 1)

    # Get the frame dimensions
    frame_height, frame_width, _ = image.shape

    # Convert the image color to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image to find hand landmarks
    output = my_hands.process(rgb_image)

    # Extract the landmarks and draw them on the image
    if output.multi_hand_landmarks:
        for hand_landmarks in output.multi_hand_landmarks:
            draw_utils.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            # Draw circles at specific finger points
            for id, landmark in enumerate(hand_landmarks.landmark):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:  # Index finger tip
                    cv2.circle(image, (x, y), 8, (0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:  # Thumb tip
                    cv2.circle(image, (x, y), 8, (0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)
        if dist > 50:
            pyg.press("volumeup")
        else:
            pyg.press("volumedown")

    # Display the image
    cv2.imshow("Hand Volume Controller", image)

    # Break the loop when 'Esc' key is pressed
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release the webcam and close the window
webcam.release()
cv2.destroyAllWindows()