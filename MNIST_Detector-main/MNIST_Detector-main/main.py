import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# -----------------------------
# Preprocessing
# -----------------------------

# Normalize pixel values (0–255 → 0–1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Flatten images from 28x28 → 784
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

# -----------------------------
# Build Neural Network
# -----------------------------

model = keras.Sequential([

    # Input layer (784 features)
    layers.Dense(128, activation='relu', input_shape=(784,)),

    # Hidden layer
    layers.Dense(64, activation='relu'),

    # Output layer (10 digits)
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
print("Test accuracy:", accuracy)

# Save trained model
model.save("mnist_model.h5")

print("Model saved as mnist_model.h5")