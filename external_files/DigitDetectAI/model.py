from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
import numpy as np
import tensorflow as tf
from flask_cors import CORS
from flask import render_template
import os

app = Flask(__name__)
CORS(app)

model_path = "/Users/sungwookmin30/Documents/GitHub/sungwookm.github.io/external_files/DigitDetectAI/digit_detect_ai.keras"
model = tf.keras.models.load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/')
#def home():
#    return "Welcome to the digit prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    image_data = data['image'].split(',')[1]
    image_data = base64.b64decode(image_data)
    
    with io.BytesIO(image_data) as f:
        img = Image.open(f).convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to the same size as the MNIST dataset images
    
    img_arr = np.array(img)
    img_arr = img_arr.reshape(1, 28, 28, 1)
    img_arr = img_arr / 255.0  # Normalize
    
    prediction = model.predict(img_arr)
    predicted_digit = np.argmax(prediction)
    
    return jsonify({"digit": int(predicted_digit)})

if __name__ == '__main__':
    app.run(debug=True)
