# Advertising Sales Predictor — Streamlit App

This project contains a production-ready Streamlit app for predicting advertising-driven sales using a Random Forest Regression model.

Quick start

```bash
python -m pip install -r requirements.txt
python model/train_model.py
streamlit run app.py
```

If `model/random_forest_model.pkl` is missing the app will attempt a lightweight fallback training on the dataset.
