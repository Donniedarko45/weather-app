# app/models/evaluation.py

from sklearn.metrics import mean_squared_error

def evaluate_vae(vae_model, test_data):
    predictions = vae_model.predict(test_data)
    return mean_squared_error(test_data, predictions)
