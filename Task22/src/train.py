import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv("data/football_players.csv")


# Separate features and target
X = data.drop(["Name", "Position"], axis=1)
y = data["Position"]


# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Test model
prediction = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    prediction
)


print("Model Accuracy:", accuracy)

print(
    classification_report(
        y_test,
        prediction
    )
)


# Save model
import os

os.makedirs("../models", exist_ok=True)


joblib.dump(
    model,
    "models/football_position_model.pkl"
)


joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)


print("Model saved successfully!")