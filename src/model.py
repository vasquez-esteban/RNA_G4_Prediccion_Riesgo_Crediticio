# credit_scoring.py

import os

import joblib  # type: ignore
import numpy as np  # type: ignore
from tensorflow.keras.models import load_model  # type: ignore

# --- Cargar recursos al inicializar módulo ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "files", "output")

scaler_minmax = joblib.load(os.path.join(OUTPUT_DIR, "scaler_minmax.pkl"))
scaler_robust = joblib.load(os.path.join(OUTPUT_DIR, "scaler_robust.pkl"))
scaler_subgrade = joblib.load(os.path.join(OUTPUT_DIR, "scaler_subgrade.pkl"))
valores_defecto = joblib.load(os.path.join(OUTPUT_DIR, "valores_defecto.pkl"))
modelo = load_model(os.path.join(OUTPUT_DIR, "modelo_riesgo_crediticio_final.h5"))


def construir_X_user(
    ordered_user, valores_defecto, scaler_minmax, scaler_robust, scaler_subgrade
):
    minmax_cols = list(scaler_minmax.feature_names_in_)
    robust_cols = list(scaler_robust.feature_names_in_)

    minmax_index = {col: i for i, col in enumerate(minmax_cols)}
    robust_index = {col: i for i, col in enumerate(robust_cols)}

    user_dict = {i: (col, val) for i, col, val in ordered_user}
    X_user = []

    for i, val in enumerate(valores_defecto):
        if isinstance(val, tuple):
            colname = val[1]

            if i in user_dict:
                user_val = user_dict[i][1]

                if colname in minmax_index:
                    dummy_input = np.zeros((1, len(minmax_cols)))
                    idx = minmax_index[colname]
                    dummy_input[0, idx] = user_val
                    scaled_val = scaler_minmax.transform(dummy_input)[0][idx]
                    X_user.append(scaled_val)

                elif colname in robust_index:
                    dummy_input = np.zeros((1, len(robust_cols)))
                    idx = robust_index[colname]
                    dummy_input[0, idx] = user_val
                    scaled_val = scaler_robust.transform(dummy_input)[0][idx]
                    X_user.append(scaled_val)

                elif colname == "sub_grade":
                    scaled_val = scaler_subgrade.transform([[user_val]])[0][0]
                    X_user.append(scaled_val)

                else:
                    X_user.append(user_val)
            else:
                X_user.append(0)
        else:
            X_user.append(val)

    return np.array(X_user).reshape(1, -1)


def prob_to_score(prob, min_score=300, max_score=850):
    return (1 - prob) * (max_score - min_score) + min_score


def predecir_score_crediticio(input_dict: dict) -> dict:
    """
    Recibe un diccionario con los valores del usuario y devuelve probabilidad y score.
    """
    # Calcular sin y cos de issue_month
    issue_month = int(input_dict["issue_month"])
    sin_val = np.sin(2 * np.pi * issue_month / 12)
    cos_val = np.cos(2 * np.pi * issue_month / 12)

    # Convertir a ordered_user
    ordered_user = [
        (0, "loan_amnt", input_dict["loan_amnt"]),
        (1, "int_rate", input_dict["int_rate"]),
        (2, "installment", input_dict["installment"]),
        (3, "sub_grade", input_dict["sub_grade"]),
        (4, "annual_inc", input_dict["annual_inc"]),
        (5, "dti", input_dict["dti"]),
        (6, "delinq_2yrs", input_dict["delinq_2yrs"]),
        (7, "inq_last_6mths", input_dict["inq_last_6mths"]),
        (8, "open_acc", input_dict["open_acc"]),
        (10, "revol_bal", input_dict["revol_bal"]),
        (11, "revol_util", input_dict["revol_util"]),
        (12, "total_acc", input_dict["total_acc"]),
        (16, "tot_cur_bal", input_dict["tot_cur_bal"]),
        (17, "total_rev_hi_lim", input_dict["total_rev_hi_lim"]),
        (18, "issue_month_sin", sin_val),
        (19, "issue_month_cos", cos_val),
        (23, "has_coll_amt", input_dict["has_coll_amt"]),
        (24, "term_ 60 months", input_dict["term_ 60 months"]),
        (35, "emp_length_Unknown", input_dict["emp_length_Unknown"]),
        (36, "home_ownership_MORTGAGE", input_dict["home_ownership_MORTGAGE"]),
    ]

    X_user = construir_X_user(
        ordered_user, valores_defecto, scaler_minmax, scaler_robust, scaler_subgrade
    )
    prob = modelo.predict(X_user)[0][0]
    score = prob_to_score(prob)

    return {"prob_default": round(prob, 4), "score_crediticio": int(round(score))}
