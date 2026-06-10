import streamlit as st
from app_pages import home, prediction, analytics, model_performance, about
from utils import load_css, load_model

st.set_page_config(page_title='Advertising Sales Predictor', layout='wide', initial_sidebar_state='expanded')

if 'theme' not in st.session_state:
    st.session_state['theme'] = 'dark'
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

load_css('assets/styles.css', st.session_state['theme'])

MENU_ITEMS = ['Home', 'Prediction', 'Analytics', 'Model Performance', 'About Project']

with st.sidebar:
    st.markdown('<div class="sidebar-brand"><h2>Ad Sales AI</h2><p>Smart budget forecasting for modern marketing teams.</p></div>', unsafe_allow_html=True)
    st.markdown('---')
    page = st.radio('Navigation', MENU_ITEMS, index=MENU_ITEMS.index(st.session_state['page']), label_visibility='collapsed')
    st.markdown('---')
    st.markdown('<div class="sidebar-support"><strong>Pro tips</strong><ul><li>Use sliders for instant budget control</li><li>Review analytics for channel impact</li><li>Deploy budgets with confidence</li></ul></div>', unsafe_allow_html=True)
    st.caption('Built with Streamlit · Random Forest')

st.session_state['page'] = page
model = load_model('model/random_forest_model.pkl')

if page == 'Home':
    home.render()
elif page == 'Prediction':
    prediction.render(model)
elif page == 'Analytics':
    analytics.render(model)
elif page == 'Model Performance':
    model_performance.render(model)
elif page == 'About Project':
    about.render()
