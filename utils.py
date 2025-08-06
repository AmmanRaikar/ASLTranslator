import mediapipe as mp
import numpy as np
import cv2

mp_hands = mp.solutions.hands

def extract_hand_landmarks(image):
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1) as hands:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            landmarks = [[lm.x, lm.y, lm.z] for lm in hand.landmark]
            return np.array(landmarks).flatten().tolist()
        else:
            return None
