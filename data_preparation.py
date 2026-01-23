import pandas as pd

def load_and_prepare_data(filepath: str, nrows: int = None):
    """
    Excel dosyasını okur, RFM hesaplaması yapar ve döndürür.
    """
    # 1. Excel verisini oku
    df = pd.read_excel(filepath, engine="openpyxl", nrows=nrows)

    # 2. Temizlik işlemleri
    df = df[pd.notnull(df["CustomerID"])]
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # 3. Bugünkü tarih
    today_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    # 4. RFM hesapla
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (today_date - x.max()).days,
        "InvoiceNo": "nunique",
        "TotalPrice": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]
    return rfm
