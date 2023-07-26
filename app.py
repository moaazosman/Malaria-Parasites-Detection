from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import tensorflow as tf
import time

# Load the machine learning model
model = tf.keras.models.load_model('malaria_model.h5')

# Create a Flask application
app = Flask(__name__, static_folder='static')

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        # Get the uploaded image file
        image_file = request.files['image']
        if image_file:
            # Open and preprocess the image
            img = Image.open(image_file)
            img = img.resize((64, 64))
            img = np.array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            # Show loading circle
            time.sleep(2)  # Simulating prediction delay

            # Perform the prediction
            prediction = model.predict(img)
            result = 'Not Infected' if prediction > 0.5 else 'Infected'

            # Render the template with the result and image filename
            return render_template('web.html', result=result, image_file=image_file.filename)

    # Render the template without any result or image filename
    return render_template('web.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
