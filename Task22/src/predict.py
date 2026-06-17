import pandas as pd
import joblib


# Load model
model = joblib.load(
    "models/football_position_model.pkl"
)


encoder = joblib.load(
    "models/label_encoder.pkl"
)


# New player data
player = pd.DataFrame([{

    "Age": 24,
    "Height": 180,
    "Weight": 75,
    "Speed": 90,
    "Passing": 82,
    "Shooting": 85,
    "Defense": 40,
    "Goals": 15,
    "Assists": 10

}])


# Prediction
prediction = model.predict(player)


position = encoder.inverse_transform(
    prediction
)


print(
    "Predicted Position:",
    position[0]
)