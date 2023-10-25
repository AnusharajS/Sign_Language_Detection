import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model
model = tf.keras.models.load_model('final_model.h5')

# Capture the video stream
cap = cv2.VideoCapture(0)
result = 'NaN'
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = result
    org = (50, 50)
    font_scale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(frame, text, org, font, font_scale,
                color, thickness, cv2.LINE_AA)
    cv2.imshow('ML_mini_project', frame)

    # Preprocess the frame
    # Resize the frame to match the input size of the model
    frame = cv2.resize(frame, (200, 200))
    # frame = frame / 255.0 # Normalize the pixel values
    # Add an extra dimension to match the input shape of the model
    frame = tf.expand_dims(frame, axis=0)
    plt.imshow(frame)
    # Make predictions on the frame
    predictions = model.predict(frame)
    class_label = np.argmax(predictions, axis=1)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = values[class_label[0]-1]

    # Display the results on the video stream
    # ...

    # Exit the loop if the user presses the 'q' key

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
