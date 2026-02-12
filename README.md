**💰 SmartPremium: Predicting Insurance Costs with Machine Learning**

📌 Project Overview : SmartPremium is an end-to-end Machine Learning project that predicts insurance premium amounts based on customer demographics, financial information, and policy details.

This project demonstrates the complete ML lifecycle:
Data preprocessing
Exploratory Data Analysis (EDA)
Model training & evaluation
Model comparison
Deployment using Streamlit

🎯 Problem Statement:
Insurance companies need accurate premium estimation to balance profitability and risk management. Manual pricing methods are inefficient and may not capture complex relationships in data.
This project builds a machine learning model that predicts insurance premium amounts using customer and policy-related features.

📊 Dataset Information
📁 Format: CSV
📈 Records: 2L+ rows
🔢 Features: 20+ (Numerical + Categorical)
🎯 Target Variable: Premium Amount

Example Features:
Age
Annual Income
Health Score
Credit Score
Previous Claims
Policy Type
Insurance Duration
Vehicle Age

🔍 Exploratory Data Analysis (EDA) Performed:
Missing value analysis
Distribution plots
Bivariate analysis
Correlation heatmap
Outlier detection

Insights:
Premium Amount is right-skewed
Income and Previous Claims positively influence premium
Some features required median/mode imputation

⚙️ Data Preprocessing
Missing values handled using:
Median (numerical features)
Mode (categorical features)
One-Hot Encoding for categorical variables
Standard Scaling for numerical variables
Implemented using Scikit-learn Pipeline
Prevented data leakage using ColumnTransformer

🤖 Models Implemented
Linear Regression (Baseline)
Random Forest Regressor
XGBoost Regressor (Final Selected Model)

📈 Model Evaluation Metrics
MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score

Final Model Selection:
XGBoost was selected based on:
Lowest RMSE
Lowest MAE
Highest R² Score

🚀 Model Deployment
Model saved using joblib
Deployed using Streamlit
Built a web app for real-time insurance premium prediction

Run locally:
streamlit run app.py

🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
XGBoost
Matplotlib & Seaborn
Streamlit
Git & GitHub

📂 Project Structure
smartpremium/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│
├── SmartPremium_EDA.ipynb
├── app.py
├── smartpremium_model.pkl
├── README.md
└── requirements.txt

🧠 Key Learnings
Handling real-world messy datasets
Feature engineering techniques
Model comparison & evaluation
Pipeline implementation
Avoiding data leakage
Deploying ML models using Streamlit

🔮 Future Improvements
Hyperparameter tuning using GridSearchCV
Cross-validation
Feature importance analysis
Cloud deployment (AWS / Streamlit Cloud)
Model monitoring

⭐ Final Summary
SmartPremium is a complete machine learning solution that demonstrates how data science can be applied to solve real-world insurance pricing problems using advanced regression techniques and deployment strategies.
