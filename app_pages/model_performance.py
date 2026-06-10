import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pathlib import Path
from sklearn import metrics

BASE_DIR = Path(__file__).resolve().parent.parent

def render(model):
    st.markdown("<div class='section-title'><h1>Model Performance</h1><p>Review accuracy, stability, and how the model performs on held-out data.</p></div>", unsafe_allow_html=True)

    try:
        import joblib
        pkg = joblib.load(BASE_DIR.joinpath('model/random_forest_model.pkl'))
    except Exception:
        pkg = None

    if pkg and 'X_test' in pkg and 'y_test' in pkg and 'model' in pkg:
        X_test = pkg['X_test']
        y_test = pkg['y_test']
        y_pred = pkg['model'].predict(X_test)
        r2 = metrics.r2_score(y_test, y_pred)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        rmse = metrics.mean_squared_error(y_test, y_pred) ** 0.5
        ev = metrics.explained_variance_score(y_test, y_pred)

        metric_cols = st.columns(4)
        metric_cols[0].metric('R² Score', f'{r2:.3f}')
        metric_cols[1].metric('MAE', f'{mae:.3f}')
        metric_cols[2].metric('RMSE', f'{rmse:.3f}')
        metric_cols[3].metric('Explained Variance', f'{ev:.3f}')

        st.markdown('<div class="card"><h3>Actual vs Predicted</h3></div>', unsafe_allow_html=True)
        df = X_test.copy()
        df['Actual'] = y_test
        df['Predicted'] = y_pred
        fig = px.scatter(df, x='Actual', y='Predicted', labels={'Actual': 'Actual Sales', 'Predicted': 'Predicted Sales'})
        x_vals = df['Actual'].to_numpy()
        y_vals = df['Predicted'].to_numpy()
        slope, intercept = np.polyfit(x_vals, y_vals, 1)
        sorted_idx = np.argsort(x_vals)
        fig.add_trace(
            go.Scatter(
                x=x_vals[sorted_idx],
                y=slope * x_vals[sorted_idx] + intercept,
                mode='lines',
                name='Trendline',
                line=dict(color='firebrick', dash='dash')
            )
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info('No test metrics found. Run the training script to generate model and metrics.')
