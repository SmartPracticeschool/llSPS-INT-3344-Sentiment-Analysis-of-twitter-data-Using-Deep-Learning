import pickle
import numpy as np
from tensorflow.keras.models import load_model


def brain(x):
    model = load_model('model.h5')
    with open('cv.pkl', 'rb') as file:
        cv = pickle.load(file)
        x = cv.transform([x])
        pred = model.predict(x)
        if(pred > 0.5):
            return f"Postive with confidence {round(pred[0][0]*100,2)}"
        else:
            return f"Negative with confidence {round(100-pred[0][0]*100,2)}"
