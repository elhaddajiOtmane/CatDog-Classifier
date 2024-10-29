from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

# Function to preprocess the image
def prepare_image(image):
    image = image.resize((224, 224))  # Resize to the model's input size
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array / 255.0  # Normalize

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Read and preprocess the image
    image = Image.open(io.BytesIO(file.read()))
    image = prepare_image(image)

    # Make predictions
    predictions = model.predict(image)
    class_idx = np.argmax(predictions, axis=1)[0]
    class_label = "Dog" if class_idx == 1 else "Cat"

    return f'The image is a: {class_label}'

if __name__ == '__main__':
    app.run(debug=True)
