import streamlit as st

def render():
    st.markdown("<div class='section-title'><h1>About the Project</h1><p>Modern advertising forecasting with a clean design and actionable insights.</p></div>", unsafe_allow_html=True)

    st.markdown('''
        <div class='glass-panel'>
            <h3>Advertising Sales Predictor</h3>
            <p>This application predicts sales from advertising budgets using a trained Random Forest Regression model. It combines interactive controls, modern insights, and polished visualizations in one app.</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('### What this app does')
    st.write('The dashboard helps marketing teams estimate how ad spend across TV, Radio, and Newspaper channels drives sales, then shows the model performance and data insights.')

    st.markdown('### Workflow')
    st.write('- Load advertising data and inspect trends')
    st.write('- Train a Random Forest regression model')
    st.write('- Generate live sales predictions from budget scenarios')
    st.write('- Review analytics and performance metrics')

    st.markdown('### Technology Stack')
    st.write('- Python')
    st.write('- scikit-learn')
    st.write('- pandas')
    st.write('- Plotly')
    st.write('- Streamlit')
