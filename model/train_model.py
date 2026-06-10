"""
Train Random Forest model on advertising_dataset.csv and save a packaged pickle.
Usage: python model/train_model.py
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / 'advertising_dataset.csv'
OUT = ROOT / 'model'
OUT.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    X = df[['TV','Radio','Newspaper']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    m = RandomForestRegressor(n_estimators=200, random_state=42)
    m.fit(X_train, y_train)
    y_pred = m.predict(X_test)
    metrics_dict = {
        'r2': metrics.r2_score(y_test, y_pred),
        'mae': metrics.mean_absolute_error(y_test, y_pred),
        'rmse': metrics.mean_squared_error(y_test, y_pred) ** 0.5,
        'explained_variance': metrics.explained_variance_score(y_test, y_pred)
    }
    pkg = {'model': m, 'metrics': metrics_dict, 'X_test': X_test, 'y_test': y_test}
    joblib.dump(pkg, OUT / 'random_forest_model.pkl')
    print('Model trained and saved to', OUT / 'random_forest_model.pkl')
    print(metrics_dict)

if __name__ == '__main__':
    main()
