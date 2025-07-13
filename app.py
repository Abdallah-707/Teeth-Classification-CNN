import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load the trained model
try:
    model = load_model('teeth_classification.h5')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define the class names
CLASS_NAMES = ['CaS', 'CoS', 'Gum', 'MC', 'OC', 'OLP', 'OT']

st.title("🦷 Teeth Disease Classification")

st.markdown("""
Upload an image of a tooth, and the model will predict the type of disease.
""")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Open and preprocess the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Resize to the model's expected input size
        image = image.resize((224, 224))
        
        # Convert the image to a numpy array and scale it
        image_array = np.array(image)
        image_array = image_array / 255.0
        
        # Add a batch dimension
        image_array = np.expand_dims(image_array, axis=0)

        # Make a prediction
        prediction = model.predict(image_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class_name = CLASS_NAMES[predicted_class_index]
        confidence = np.max(prediction)

        st.write("")
        st.write("### Prediction:")
        st.success(f"The model predicts that the tooth has **{predicted_class_name}** with a confidence of **{confidence:.2f}**.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")