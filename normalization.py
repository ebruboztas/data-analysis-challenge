from sklearn.preprocessing import StandardScaler
import pandas as pd

def normalize_rfm(rfm_df):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df)
    return pd.DataFrame(rfm_scaled, columns=rfm_df.columns, index=rfm_df.index)
