from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def plot_elbow(rfm_scaled_df, max_k=10):
    sse = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(rfm_scaled_df)
        sse.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_k + 1), sse, marker='o')
    plt.xlabel("Küme Sayısı (K)")
    plt.ylabel("SSE (Hata)")
    plt.title("Elbow Yöntemi ile Optimal Küme Sayısı")
    plt.grid(True)
    plt.show()

def apply_kmeans(rfm_scaled_df, k):
    model = KMeans(n_clusters=k, random_state=42)
    return model.fit_predict(rfm_scaled_df)
