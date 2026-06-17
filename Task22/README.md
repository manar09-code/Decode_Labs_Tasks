# ⚽ Football Player Position Classification Using AI

## DecodeLabs Artificial Intelligence Project 2

This project implements a supervised machine learning classification model that predicts a football player's position based on their performance statistics.

The objective is to build a complete AI pipeline including:

- Dataset preparation
- Data preprocessing
- Training/testing split
- Machine learning model training
- Model evaluation
- Prediction on new data


## Project Goal

The model classifies football players into four categories:

- Goalkeeper
- Defender
- Midfielder
- Forward


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib


## Dataset Features

The dataset contains football player statistics:

| Feature | Description |
|---|---|
| Age | Player age |
| Height | Player height |
| Weight | Player weight |
| Speed | Player speed rating |
| Passing | Passing ability |
| Shooting | Shooting ability |
| Defense | Defensive ability |
| Goals | Number of goals |
| Assists | Number of assists |


## Machine Learning Approach

### 1. Data Loading

The football dataset is loaded using Pandas.

### 2. Data Preparation

The target variable:


Position


is encoded using Label Encoding.

### 3. Data Splitting

The dataset is divided into:

- 80% Training data
- 20% Testing data


### 4. Model Training

The project uses:

- Random Forest Classifier


### 5. Model Evaluation

The model is evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix


## Project Structure


Task_22/

│
├── data/
│ └── football_players.csv
│
├── models/
│
├── src/
│ ├── train.py
│ └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore



## Installation

Clone the repository:

```bash
git clone <repository-url>

Install dependencies:

pip install -r requirements.txt
Training the Model

Navigate to the src folder:

cd src

Run:

python train.py
Making Predictions

Run:

python predict.py
Results

The trained model can classify football players into their expected playing positions based on statistical features.

Author
Manar Degachi
AI Engineering Intern
DecodeLabs Internship Program 2026


---

## Commands to run after creating files

From `Task_22`:

```powershell
venv\Scripts\activate
pip install -r requirements.txt

Train:

cd src
python train.py

Predict:

python predict.py