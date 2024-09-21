# app/models/save_model.py
import tensorflow as tf

def save_model(model, filename):
    model.save(filename)

def load_model(filename):
    return tf.keras.models.load_model(filename)

