# 🧠 ASL Hand Gesture Translator (Web App)

A real-time American Sign Language (ASL) hand gesture recognition web app that uses machine learning and computer vision to translate static gestures into text. This project supports webcam input and displays live predictions with visual feedback.

## 🌐 Live Demo

[ASLTranslator](https://asltranslator-o0yb.onrender.com/)  

## 📸 Features

- 🖐️ Real-time hand detection using MediaPipe
- 🔤 Alphabet and digit prediction using a pre-trained model
- 🎯 Clean and responsive UI
- 💡 Lightweight and easy to deploy

## 🚀 Quick Start

To run locally:

### 1. Clone the repository
```bash
git clone https://github.com/AmmanRaikar/ASLTranslator.git
cd ASLTranslator
```

### 2. Install dependencies
It's recommended to use a Python 3.11.4 virtual environment. 
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Then open your browser and go to:  
[http://localhost:5000](http://localhost:5000)

## 📁 Project Structure

```
/models/
    model.pkl             # Pre-trained gesture recognition models
    label_map.json        # Labels for trained model
/static/
    style.css
    script.js
/templates/
    index.html           # Main HTML UI
app.py                   # Flask server
utils.py                 # Prediction Function
requirements.txt
```

## 🤖 Technologies Used

- Python & Flask
- TensorFlow / Keras
- MediaPipe
- OpenCV
- HTML, CSS, JavaScript

## 📌 Notes

- The model currently supports **static ASL hand gestures** (A–Z and 0–9).
- Dynamic gestures (e.g., words like "Hello", "Thank you") are not yet supported.

---

> 🛠️ Built with passion to make sign language more accessible.
> Be sure to Credit my work, if featured or used.
