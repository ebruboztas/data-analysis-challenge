def analyze_segments(rfm_df):
    return rfm_df.groupby("Cluster").mean().round(2)
