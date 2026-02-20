# core/gender_prediction.py

import joblib
import numpy as np

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")


def predict_gender(measurements):
    """
    Use ONLY Left sinus volume.
    measurements["Left"] format:
    (Volume_mm3, Length, Height, Breadth)
    """

    if not measurements:
        return None, None

    if "Left" not in measurements or measurements["Left"] is None:
        return None, None

    left_tuple = measurements["Left"]

    # ✅ Volume is FIRST element
    left_volume = float(left_tuple[0])

    if left_volume <= 2000:
        return None, None

    X = np.array([[left_volume]])
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    gender = "Male" if prediction == 1 else "Female"

    return gender, float(probability)
