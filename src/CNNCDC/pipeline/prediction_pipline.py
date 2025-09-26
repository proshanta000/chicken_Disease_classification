import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Load the model only once when the class is initialized for efficiency
        # Ensure this path is correct for your project structure
        self.model = load_model(os.path.join("artifacts", "training", "model.h5"))
        
        # Define the class names. IMPORTANT: These must match the order 
        # that Keras/TensorFlow determined during training (alphabetical by folder name).
        self.class_names = ['Coccidiosis', 'Healthy']

    def predict(self):
        imagename = self.filename
        try:
            # Load the image and resize it to the expected input size (e.g., 224x224)
            test_image = image.load_img(imagename, target_size=(224, 224))
        except FileNotFoundError:
            # Return a clear error message in the expected list format
            return [{"label": "Error: Image file not found.", "confidence": 0.0}]
        except Exception as e:
            return [{"label": f"Error loading image: {e}", "confidence": 0.0}]

        # Preprocessing
        test_image = image.img_to_array(test_image)
        # Normalize the image pixels to the range [0, 1]
        test_image = test_image / 255.0
        # Expand dimensions to create a batch (1, 224, 224, 3)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Make the prediction
        # predictions will be an array like [[0.05, 0.95]]
        predictions = self.model.predict(test_image)
        
        # Find the index of the highest probability
        result_index = np.argmax(predictions, axis=1)[0]
        
        # Extract the confidence score (the actual probability value)
        # We cast it to a standard Python float for JSON serialization
        confidence_score = float(predictions[0][result_index]) 
        
        # Get the predicted class name
        prediction_label = self.class_names[result_index]
        
        print(f"Prediction result index: {result_index}")
        print(f"Predicted class: {prediction_label}")
        print(f"Confidence score: {confidence_score}")

        # --- CRITICAL FIX: Returning the correct dictionary structure ---
        # The Flask app expects result[0] to have 'label' and 'confidence'
        return [{
            "label": prediction_label,
            "confidence": confidence_score
        }]
