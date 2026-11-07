# 🎓 Student Score Prediction System

## 📌 Project Overview

The **Student Score Prediction System** is a Machine Learning-based application that predicts a student's expected exam score based on the number of hours they study.

The project implements and compares multiple regression algorithms to identify the best-performing model. It also provides an interactive Gradio interface where users can enter their study hours and receive a predicted score.

## ✨ Features

- 📚 Predict student exam scores based on study hours.
- 🤖 Implement multiple Machine Learning regression algorithms.
- 📊 Compare model performance using evaluation metrics.
- 📈 Visualize the relationship between study hours and exam scores.
- 🔍 Compare actual and predicted scores.
- 🏆 Automatically select the best-performing regression model based on R² score.
- 💻 Interactive prediction interface using Gradio.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Joblib
- Gradio

## 🧠 Machine Learning Algorithms

The following algorithms are implemented:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regression
5. Random Forest Regression

## 📊 Model Evaluation

The models are evaluated using:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

The model with the highest R² score is selected as the best-performing model.

## 📸 Application Screenshots

### 1. Prediction Interface
<img width="1457" height="729" alt="image" src="https://github.com/user-attachments/assets/1fa0af91-1883-4949-9136-19673707c65a" />


### 2. Prediction Output
<img width="1464" height="731" alt="image" src="https://github.com/user-attachments/assets/7e56ccfe-26d8-449e-bdd3-cdf6c4899663" />


## 📂 Project Structure

```text
Student-Score-Prediction/
│
├── app.py
├── student_score_prediction.ipynb
├── best_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── dataset.png
    ├── model-comparison.png
    ├── regression-plot.png
    ├── home.png
    └── prediction.png
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Student-Score-Prediction
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python app.py
```

## 🎯 How It Works

1. The dataset containing study hours and exam scores is prepared.
2. Data is explored and visualized.
3. Multiple regression models are trained.
4. Model performance is evaluated using regression metrics.
5. The best-performing model is selected.
6. The trained model is saved using Joblib.
7. Users enter their study hours through the Gradio interface.
8. The application displays the predicted exam score.

## 👩‍💻 Project Objective

The objective of this project is to understand and implement regression-based Machine Learning techniques for predicting student academic performance and comparing different predictive models.

---

⭐ If you find this project useful, consider giving it a star!
