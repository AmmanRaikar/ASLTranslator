from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
import json
import os
from utils import extract_hand_landmarks
import joblib
import mediapipe as mp


app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'models/asl_model.pkl')
labels_path = os.path.join(os.path.dirname(__file__), 'models/label_map.json')

with open(model_path, 'rb') as f:
    model = joblib.load(model_path)

with open(labels_path, 'r') as f:
    label_map = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['image']
        encoded_data = data.split(',')[1]
        img_data = base64.b64decode(encoded_data)
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        img = cv2.flip(img, 1)

        # DEBUGGING:
        cv2.imwrite("latest_frame.jpg", img)
        print("[INFO] Frame received")

        landmarks = extract_hand_landmarks(img)

        if landmarks:
            prediction = model.predict([landmarks])[0]
            label = label_map.get(str(int(prediction)), str(prediction))
            mp_hands = mp.solutions.hands
            mp_drawing = mp.solutions.drawing_utils

            # Draw landmarks
            with mp_hands.Hands(static_image_mode=False, max_num_hands=1) as hands:
                results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            img, hand_landmarks, mp_hands.HAND_CONNECTIONS
                        )
        else:
            label = "No hands detected"

        # Encode frame back to base64
        _, buffer = cv2.imencode('.jpg', img)
        annotated_image = base64.b64encode(buffer).decode('utf-8')

        return jsonify({'prediction': label, 'image': f"data:image/jpeg;base64,{annotated_image}"})

    except Exception as e:
        print("[ERROR]", str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env var for deployment
    app.run(host='0.0.0.0', port=port, debug=False)
