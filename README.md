# 💼 Salary Prediction

A machine learning model that predicts employee salaries based on experience, test scores, and interview scores using **Linear Regression**.

---

## 📌 Overview

This project uses a hiring dataset to train a regression model that estimates the expected salary of a candidate. Missing data is handled intelligently before training, and the final model is serialized for reuse.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn
- **Model:** Linear Regression
- **Serialization:** Pickle

---

## 📂 Dataset

The dataset (`hiring.csv`) contains the following features:

| Feature | Description |
|---|---|
| `experience` | Years of experience (in words, e.g. *"two"*) |
| `test_score` | Aptitude test score |
| `interview_score` | Interview performance score |
| `salary` | Target variable — expected salary |

> Missing `experience` values are filled with `0`; missing `test_score` values are filled with the column mean.

---
<!--
## 🚀 How It Works

1. Load and preprocess the dataset
2. Convert experience from words → integers
3. Train a `LinearRegression` model on all available data
4. Save the model using `pickle`
5. Load and use the model to predict salaries

```python
model.predict([[2, 9, 6]])  # [experience, test_score, interview_score]
```
-->