import cv2
import numpy as np

# Path to MRI image
image_path = "sample_mri.jpg"

# Load image
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image to model input size (Example: 224x224)
image = cv2.resize(image, (224, 224))

# Convert image to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Normalize pixel values
image = image.astype("float32") / 255.0

# Add batch dimension
image = np.expand_dims(image, axis=0)

print("Image Shape:", image.shape)
