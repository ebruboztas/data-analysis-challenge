from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Cem'in yazdığı modülleri (motoru) içeri aktarıyoruz
from data_preparation import load_and_prepare_data
from normalization import normalize_rfm
from clustering import apply_kmeans

app = Flask(__name__)

@app.route('/')
def index():
    # 1. Veriyi yükle (Cem'in 10.000 satır sınırı ile hızlı analiz)
    rfm = load_and_prepare_data("Online Retail.xlsx", nrows=10000)
    
    # 2. Normalizasyon ve K-Means (Cem'in belirlediği k=4 küme ile)
    rfm_scaled_df = normalize_rfm(rfm)
    rfm['Cluster'] = apply_kmeans(rfm_scaled_df, k=4)
    
    # 3. İnteraktif 3D Grafiği (SAYZA Dashboard için)
    fig = px.scatter_3d(rfm, x='Recency', y='Frequency', z='Monetary', 
                        color='Cluster', title='SAYZA: Müşteri Segmentasyonu')
    graph_html = pio.to_html(fig, full_html=False)
    
    # Dashboard verilerini arayüze gönderiyoruz
    return render_template('index.html', 
                           tablo=rfm.head(10).to_html(classes='table table-striped'), 
                           grafik=graph_html,
                           toplam_musteri=len(rfm))

if __name__ == '__main__':
    app.run(debug=True)
