import streamlit as st

def render():
    st.markdown(
        '''
        <div class="hero-grid">
            <div class="hero-copy">
                <span class="eyebrow">Next-gen forecast dashboard</span>
                <h1>Advertising Sales Predictor</h1>
                <p class="subtitle">Estimate sales with a powerful Random Forest model, visualize channel effectiveness, and shape better campaigns with a modern analytics experience.</p>
            </div>
            <div class="hero-image">
                <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=900&q=80" alt="Marketing Dashboard">
            </div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<div class="section-panel"><div class="section-grid"><div class="feature-card"><h3>Instant forecasts</h3><p>Rapid sales predictions from your budget mix, with clear confidence metrics.</p></div><div class="feature-card"><h3>Data-driven insights</h3><p>Explore correlations, feature importance, and spend efficiency in one place.</p></div><div class="feature-card"><h3>Modern interface</h3><p>A clean, professional dashboard styled for polished presentations.</p></div></div></div>', unsafe_allow_html=True)

    st.markdown('---')
    st.subheader('Why this app stands out')
    st.markdown('''
        <div class="data-card">
            <div><span class="accent">•</span> Responsive layout built for desktop and tablet screens.</div>
            <div><span class="accent">•</span> Lightweight prediction flow with instant feedback.</div>
            <div><span class="accent">•</span> Actionable insights for marketing planners immediately.</div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('---')
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="stat-card"><h3>Ready to use</h3><p>Load and predict in seconds.</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="stat-card"><h3>Interactive</h3><p>Sliders, charts, and visual summaries.</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="stat-card"><h3>Beautiful</h3><p>Modern UI with polished card panels.</p></div>', unsafe_allow_html=True)

    st.markdown('---')
    start_col, analytics_col = st.columns(2)
    with start_col:
        if st.button('Start Predicting', key='hero_predict'):
            st.session_state['page'] = 'Prediction'
            if hasattr(st, 'rerun'):
                st.rerun()
            elif hasattr(st, 'experimental_rerun'):
                st.experimental_rerun()
    with analytics_col:
        if st.button('View Analytics', key='hero_analytics'):
            st.session_state['page'] = 'Analytics'
            if hasattr(st, 'rerun'):
                st.rerun()
            elif hasattr(st, 'experimental_rerun'):
                st.experimental_rerun()
