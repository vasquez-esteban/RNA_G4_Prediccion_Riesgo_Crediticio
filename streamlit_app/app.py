# Ejemplo de llamada al modelo

import os
import sys

# Agregar la ruta raíz del proyecto al path (para que src sea visible)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import predecir_score_crediticio

entrada = {
    "loan_amnt": 100000,
    "int_rate": 20.0,
    "installment": 220,
    "sub_grade": 1,
    "annual_inc": 120000,
    "dti": 10.0,
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
    "term_60_months": 0,
    "emp_length_Unknown": 0,
    "home_ownership_MORTGAGE": 1,
}

resultado = predecir_score_crediticio(entrada)
print(resultado)
# {'prob_default': 0.7307, 'score_crediticio': 448}
