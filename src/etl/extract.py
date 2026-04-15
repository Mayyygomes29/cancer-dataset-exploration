import pandas as pd
import os
# =========================
# EXTRACT
# =========================
def extract():
    path = os.path.join("data", "dataR2.csv")
    return pd.read_csv(path)
    
