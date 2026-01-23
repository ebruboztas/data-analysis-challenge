from data_preparation import load_and_prepare_data
from normalization import normalize_rfm
from clustering import plot_elbow, apply_kmeans
from segment_analysis import analyze_segments

# 1. RFM hesapla
rfm = load_and_prepare_data("Online Retail.xlsx", nrows=10000)

# 2. Normalize et
rfm_scaled_df = normalize_rfm(rfm)

print("Toplam müşteri sayısı:", rfm.shape[0])

# 3. İlk sonuçları yazdır
print("\n🧾 İlk 10 müşterinin RFM değeri:")
print(rfm.head(10))

print("\n📐 Normalize edilmiş RFM değerleri:")
print(rfm_scaled_df.head(10))


# 3. Elbow grafiği çizdir (k'yi gözle belirle)
plot_elbow(rfm_scaled_df)

# 4. K seç (grafikte 4 gibi kırılma varsa)
rfm["Cluster"] = apply_kmeans(rfm_scaled_df, k=4)

# 5. Segment analizini göster
print("\n📊 Segmentlerin ortalama RFM değerleri:")
print(analyze_segments(rfm))