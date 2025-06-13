import os
import sys

import pandas as pd
import streamlit as st

# ✅ Configuración de la página
st.set_page_config(page_title="Predicción de Riesgo Crediticio", layout="centered")

# 🎨 Estilos personalizados
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #cceeff, #d1f7e3);
        background-attachment: fixed;
        color: #1a1a1a;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        text-align: center;
        color: #7b2cbf;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }

    .stButton > button {
        background-color: #00C897;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 1.1em;
        border: none;
        box-shadow: 1px 1px 5px #00000030;
        transition: 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #00a27a;
        transform: scale(1.02);
    }

    .stNumberInput input, .stSlider > div > div {
        background-color: rgba(255, 255, 255, 0.95);
        color: #1a1a1a;
        border-radius: 5px;
        padding: 5px;
    }

    .stMetric {
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        padding: 10px;
        margin-top: 20px;
        color: #1a1a1a;
    }

    div[data-testid="stMetricValue"] {
        color: rgb(0, 0, 0);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 📂 Hacer visible el módulo src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.model import predecir_score_crediticio

# 🧾 Título e instrucciones
st.title("📊 Calculadora de Score Crediticio")
st.markdown("Ingresa la siguiente información para estimar el riesgo:")

# 📥 Inputs de usuario
loan_amnt = st.number_input(f":blue[💰 Monto del préstamo]", value=100000)
int_rate = st.slider(f":blue[📈 Tasa de interés (%)]", 0.0, 30.0, 20.0)
installment = st.number_input(f":blue[📆 Cuota mensual]", value=220)
annual_inc = st.number_input(f":blue[📊 Ingreso anual]", value=120000)
dti = st.slider(f":blue[⚖️ DTI (deuda/ingreso %)]", 0.0, 40.0, 10.0)

# ▶️ Acción
if st.button("Calcular score"):
    entrada = {
        "loan_amnt": loan_amnt,
        "int_rate": int_rate,
        "installment": installment,
        "sub_grade": 1,
        "annual_inc": annual_inc,
        "dti": dti,
        "delinq_2yrs": 0,
        "inq_last_6mths": 1,
        "open_acc": 15,
        "revol_bal": 2000,
        "revol_util": 12.0,
        "total_acc": 35,
        "tot_cur_bal": 150000,
        "total_rev_hi_lim": 20000,
        "issue_month": 6,
        "has_coll_amt": 0,
        "term_ 60 months": 0,  # ⚠️ espacio intencional
        "emp_length_Unknown": 0,
        "home_ownership_MORTGAGE": 1,
    }
    resultado = predecir_score_crediticio(entrada)

    st.metric(f":blue[🎯 Score Crediticio]", resultado["score_crediticio"])
    st.write(f"💥 Probabilidad de incumplimiento: **{resultado['prob_default']:.2%}**")

# 🔗 Enlaces adicionales
st.markdown("---")
st.markdown("### 📎 Recursos Relacionados")
st.markdown(
    "- 📘 [Análisis completo en RPubs](https://rpubs.com/evasp/rna-g4-datos-tabulares)"
)
st.markdown("- ▶️ [Video explicativo en YouTube](https://www.youtube.com)")
