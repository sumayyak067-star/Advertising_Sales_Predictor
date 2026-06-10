import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def resolve_path(path: str) -> Path:
    p = Path(path)
    return p if p.is_absolute() else BASE_DIR.joinpath(path)


def load_css(path: str, theme: str = 'dark'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            css = f.read()
        if theme == 'light':
            theme_vars = """
                :root {
                    --bg:#f8fafc;
                    --panel:rgba(255,255,255,0.84);
                    --card:rgba(255,255,255,0.78);
                    --text:#111827;
                    --subtext:#475569;
                    --accent:#4338ca;
                    --btn-start:#4338ca;
                    --btn-end:#0891b2;
                }
            """
        else:
            theme_vars = """
                :root {
                    --bg:#0f1724;
                    --panel:rgba(15,23,36,0.92);
                    --card:rgba(15,23,36,0.72);
                    --text:#e2e8f0;
                    --subtext:#94a3b8;
                    --accent:#7c3aed;
                    --btn-start:#7c3aed;
                    --btn-end:#06b6d4;
                }
            """
        st.markdown(f"<style>{theme_vars}{css}</style>", unsafe_allow_html=True)
    except Exception:
        st.markdown('<style>body{font-family:Inter, system-ui;}</style>', unsafe_allow_html=True)

def load_model(pickle_path: str):
    p = resolve_path(pickle_path)
    if p.exists():
        try:
            pkg = joblib.load(str(p))
            if isinstance(pkg, dict) and 'model' in pkg:
                return pkg['model']
            return pkg
        except Exception as e:
            st.warning(f'Failed to load model pickle: {e}')
    # If not found or failed, attempt to train
    st.info('Trained model not found. Run `python model/train_model.py` to train and save model, or the app will train a lightweight fallback.')
    # fallback: quick train
    try:
        from sklearn.ensemble import RandomForestRegressor
        df_path = resolve_path('advertising_dataset.csv')
        df = pd.read_csv(df_path)
        X = df[['TV','Radio','Newspaper']]
        y = df['Sales']
        m = RandomForestRegressor(n_estimators=50, random_state=42)
        m.fit(X, y)
        return m
    except Exception as e:
        st.error(f'Unable to train fallback model: {e}')
        return None
