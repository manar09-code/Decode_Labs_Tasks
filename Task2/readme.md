# Iris Flower Classification using K-Nearest Neighbors (KNN)

## Project Overview

This project was developed as part of the DecodeLabs Artificial Intelligence Internship Program.

The goal of the project is to build a machine learning classification model capable of predicting the species of an Iris flower based on its physical measurements.

The project demonstrates the complete supervised learning workflow, including data preprocessing, model training, prediction, and evaluation.

---

## Dataset

The project uses the Iris Dataset provided by Scikit-Learn.

Features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:
- Setosa
- Versicolor
- Virginica

---

## Technologies Used

- Python 3
- Scikit-Learn
- NumPy

---

## Machine Learning Workflow

### 1. Load Dataset

The Iris dataset is loaded using Scikit-Learn.

### 2. Feature Scaling

Data is standardized using `StandardScaler()` to ensure all features contribute equally to the model.

### 3. Train-Test Split

The dataset is split into:
- 80% Training Data
- 20% Testing Data

### 4. Model Training

A K-Nearest Neighbors (KNN) classifier is trained using:

```python
KNeighborsClassifier(n_neighbors=5)
```

### 5. Prediction

The trained model predicts flower species on unseen test data.

### 6. Evaluation

Model performance is evaluated using:

- Accuracy Score
- F1 Score
- Confusion Matrix
- Classification Report

---

## Results

| Metric | Value |
|----------|----------|
| Accuracy | 93.33% |
| Weighted F1 Score | 0.93 |

Confusion Matrix:

```text
[[10 0 0]
 [0 10 0]
 [0 2 8]]
```

---

## Project Structure

```text
Task2/
│
├── proj2.py
├── README.md
└── output_screenshot.png
```

---

## Learning Outcomes

Through this project, I gained practical experience with:

- Supervised Learning
- Data Preprocessing
- Feature Scaling
- Classification Algorithms
- Model Evaluation Metrics
- Scikit-Learn Workflow

---

## Author

Manar

Artificial Intelligence Internship Program
DecodeLabs 2026