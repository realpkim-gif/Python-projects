import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("mnist_model_CNN.h5")

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Rectangle coordinates
    x1, y1 = 100, 100
    x2, y2 = 300, 300

    # Draw rectangle on screen
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Extract region of interest
    roi = frame[y1:y2, x1:x2]

    # -----------------------------
    # Preprocessing
    # -----------------------------

    # Convert to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold to isolate digit (ret is return value)

    #adaptive thresh
    # Adaptive thresholding

    thresh = cv2.adaptiveThreshold(
        blur,  # Input image (grayscale + blurred)
        255,  # Maximum value to use for white pixels
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # Use weighted mean of neighborhood
        cv2.THRESH_BINARY_INV,  # Invert: digit white, background black
        11,  # Block size: neighborhood size (must be odd)
        2  # C: subtract this constant from mean
    )

    # Resize to MNIST size
    digit = cv2.resize(thresh, (28, 28))

    # Normalize
    digit = digit / 255.0

    # Flatten
    digit = digit.reshape(1, 28,28,1)

    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(digit, verbose=0)
    digit_class = np.argmax(prediction)
    confidence = np.max(prediction)

    digit_class_label="?"
    # Display prediction
    if confidence > 0.8:
        digit_class_label = str(digit_class)
    elif confidence <=0.8:
        digit_class_label = "?"

    print(confidence)

    cv2.putText(
        frame,
        f"Prediction: {digit_class_label}",
        (100, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show windows
    cv2.imshow("Digit Recognition", frame)
    cv2.imshow("Processed Digit", thresh)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()