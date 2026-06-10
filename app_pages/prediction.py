import streamlit as st
import pandas as pd
import numpy as np

def render(model):
    st.markdown("<div class='section-title'><h1>Make a Prediction</h1><p>Set TV, Radio, and Newspaper budgets and instantly view the expected sales outcome.</p></div>", unsafe_allow_html=True)

    if 'tv_budget' not in st.session_state:
        st.session_state.tv_budget = 150.0
        st.session_state.tv_slider = 150.0
        st.session_state.tv_input = 150.0
    if 'radio_budget' not in st.session_state:
        st.session_state.radio_budget = 22.0
        st.session_state.radio_slider = 22.0
        st.session_state.radio_input = 22.0
    if 'newspaper_budget' not in st.session_state:
        st.session_state.newspaper_budget = 12.0
        st.session_state.newspaper_slider = 12.0
        st.session_state.newspaper_input = 12.0

    def sync_tv_slider():
        st.session_state.tv_budget = st.session_state.tv_slider
        st.session_state.tv_input = st.session_state.tv_slider

    def sync_tv_input():
        st.session_state.tv_budget = st.session_state.tv_input
        st.session_state.tv_slider = st.session_state.tv_input

    def sync_radio_slider():
        st.session_state.radio_budget = st.session_state.radio_slider
        st.session_state.radio_input = st.session_state.radio_slider

    def sync_radio_input():
        st.session_state.radio_budget = st.session_state.radio_input
        st.session_state.radio_slider = st.session_state.radio_input

    def sync_newspaper_slider():
        st.session_state.newspaper_budget = st.session_state.newspaper_slider
        st.session_state.newspaper_input = st.session_state.newspaper_slider

    def sync_newspaper_input():
        st.session_state.newspaper_budget = st.session_state.newspaper_input
        st.session_state.newspaper_slider = st.session_state.newspaper_input

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('TV Budget')
        st.slider(' ', 0.0, 500.0, key='tv_slider', step=1.0, on_change=sync_tv_slider, label_visibility='collapsed')
        st.number_input(' ', min_value=0.0, max_value=500.0, key='tv_input', step=1.0, on_change=sync_tv_input, label_visibility='collapsed')
    with col2:
        st.subheader('Radio Budget')
        st.slider(' ', 0.0, 500.0, key='radio_slider', step=1.0, on_change=sync_radio_slider, label_visibility='collapsed')
        st.number_input(' ', min_value=0.0, max_value=500.0, key='radio_input', step=1.0, on_change=sync_radio_input, label_visibility='collapsed')
    with col3:
        st.subheader('Newspaper Budget')
        st.slider(' ', 0.0, 500.0, key='newspaper_slider', step=1.0, on_change=sync_newspaper_slider, label_visibility='collapsed')
        st.number_input(' ', min_value=0.0, max_value=500.0, key='newspaper_input', step=1.0, on_change=sync_newspaper_input, label_visibility='collapsed')

    st.markdown('<div class="panel-grid"><div><strong>TV</strong><p>${:,.0f}</p></div><div><strong>Radio</strong><p>${:,.0f}</p></div><div><strong>Newspaper</strong><p>${:,.0f}</p></div></div>'.format(st.session_state.tv_budget, st.session_state.radio_budget, st.session_state.newspaper_budget), unsafe_allow_html=True)
    submit = st.button('Predict')

    tv = st.session_state.tv_budget
    radio = st.session_state.radio_budget
    newspaper = st.session_state.newspaper_budget

    if model is None:
        st.error('Model is not loaded. Please train the model by running `python model/train_model.py` or ensure the saved model exists in the `model/` folder.')
        return

    if submit:
        with st.spinner('Predicting...'):
            X = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
            try:
                if hasattr(model, 'predict'):
                    y_pred = model.predict(X)[0]
                    try:
                        all_preds = np.array([est.predict(X)[0] for est in model.estimators_])
                        std = float(all_preds.std())
                        conf = max(0, min(100, 100 - (std / max(1.0, abs(y_pred)) * 100)))
                    except Exception:
                        std = 0.0
                        conf = 80.0

                    st.markdown(
                        f"<div class='result-card'><h2>Forecasted Sales: <span class='accent'>{y_pred:.2f}</span></h2><p class='subtitle'>Estimated confidence: <strong>{conf:.0f}%</strong></p></div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.error('Model is not loaded correctly. The loaded object does not support predict().')
            except Exception as e:
                st.error(f'Prediction failed: {e}')
