import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def render(model):
    st.markdown("<div class='section-title'><h1>Analytics Dashboard</h1><p>Explore the dataset, discover patterns, and understand how budget decisions affect sales.</p></div>", unsafe_allow_html=True)

    try:
        df_path = BASE_DIR.joinpath('advertising_dataset.csv')
        df = pd.read_csv(df_path)
    except Exception as e:
        st.error(f'Dataset not found or failed to load: {e}')
        return

    metric_cols = st.columns(3)
    metric_cols[0].metric('Total Rows', f'{len(df):,}')
    metric_cols[1].metric('Average Sales', f'{df['Sales'].mean():.2f}')
    metric_cols[2].metric('Channels', 'TV, Radio, Newspaper')

    st.markdown('<div class="section-panel"><div class="section-grid"><div class="feature-card"><strong>Budget impact</strong><p>TV spend shows strong correlation with sales in this dataset.</p></div><div class="feature-card"><strong>Sales distribution</strong><p>Insights help identify high-performing campaigns and spend ranges.</p></div></div></div>', unsafe_allow_html=True)

    st.markdown('---')
    st.subheader('Correlation Heatmap')
    corr = df.corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu', aspect='auto')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Feature Importance')
    try:
        importances = model.feature_importances_
        feat = ['TV', 'Radio', 'Newspaper']
        fig2 = px.bar(x=feat, y=importances, labels={'x': 'Feature', 'y': 'Importance'}, color=importances, color_continuous_scale='Aggrnyl')
        st.plotly_chart(fig2, use_container_width=True)
    except Exception:
        st.info('Feature importances not available for this model.')

    st.subheader('Sales Distribution')
    fig3 = px.histogram(df, x='Sales', nbins=30, marginal='box', color_discrete_sequence=['#7C3AED'])
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader('Budget vs Sales')
    fig4 = px.scatter(df, x='TV', y='Sales', size='Radio', color='Newspaper', labels={'TV': 'TV Budget', 'Sales': 'Sales'}, title='Sales vs TV Budget')
    x_vals = df['TV'].to_numpy()
    y_vals = df['Sales'].to_numpy()
    slope, intercept = np.polyfit(x_vals, y_vals, 1)
    sorted_idx = np.argsort(x_vals)
    fig4.add_trace(
        go.Scatter(
            x=x_vals[sorted_idx],
            y=slope * x_vals[sorted_idx] + intercept,
            mode='lines',
            name='Trendline',
            line=dict(color='firebrick', dash='dash')
        )
    )
    st.plotly_chart(fig4, use_container_width=True)
