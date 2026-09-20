import os
import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import base64

app = Flask(__name__)

model = tf.keras.models.load_model('converted_keras/keras_model.h5')
class_names = [
    'අ','ආ','ඇ','ඈ','ඉ','ඊ','උ','ඌ','එ','ඒ','ඔ','ඕ','ක්','ග්','ජ්','ට්','ද්','ණ්','ත්','ඩ්','න්','ප්','බ්','ම්','ය්','ර්','ල්',
    'ව්','ස්','හ්','ළ්','o','ඟ්','ඬ්','ඳ්','ඹ්','ඛ්','ඝ්','ඪ්','ඵ්','ධ්','ඨ්','ච්','ඡ්','්‍ය','ෆ','භ','ථ්','ශ්','ෂ්','No Signs Detected'
]

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((224, 224))
    img = np.array(img).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img_data = base64.b64decode(data['image'])
    img = preprocess_image(img_data)
    predictions = model.predict(img, verbose=0)
    idx = int(np.argmax(predictions))
    confidence = float(np.max(predictions))
    return jsonify({
        'class': class_names[idx],
        'confidence': confidence
    })

@app.route("/health")
def health():
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 7861)))