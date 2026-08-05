# Smart Wellbore TVT Prediction System

## Project Description

This project was developed for the CIS6005 Computational Intelligence module.

The application predicts True Vertical Thickness (TVT) using a Tuned Extra Trees Regressor model developed from the Rogii Wellbore Geology Prediction Kaggle competition dataset.

---

## Software Requirements

- Python 3.11 or later
- Visual Studio Code (Recommended)

---

## Required Libraries

Install the following libraries before running the application:

pip install flask
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib

---

## Project Structure

TVT_Prediction_System/

├── app.py

├── extra_trees_deployment.pkl

├── templates/

│     └── index.html

├── static/

│     └── style.css

---

## Running the Application

1. Open the project folder.

2. Open Command Prompt or Terminal.

3. Run:

python app.py

4. Open the following address in your web browser:

http://127.0.0.1:5000

---

## Dataset

Rogii Wellbore Geology Prediction

https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction

---

## Author

Lakshana K

CIS6005 – Computational Intelligence


Note: The trained deployment model (extra_trees_deployment.pkl) is not included in this repository because it exceeds GitHub's file size limit. It has been provided separately as part of the assignment submission.