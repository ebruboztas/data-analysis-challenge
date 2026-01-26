# 🚀 SAYZA: 3D Müşteri Segmentasyonu & RFM Analizi

SAYZA, karmaşık perakende verilerini anlamlı pazarlama stratejilerine dönüştüren interaktif bir veri analizi dashboard'udur. Bu proje, **YZTA 72 Saatlik Veri Analizi Challenge** kapsamında geliştirilmiştir.

## 📊 Proje Özeti
Uygulama, **303 farklı müşterinin** geçmiş alışveriş verilerini (Online Retail) analiz ederek onları davranışsal benzerliklerine göre gruplandırır. İşletmelerin en sadık müşterilerini tanımasını ve pazarlama stratejilerini veriye dayalı yönetmesini sağlar.

### Öne Çıkan Özellikler:
* **RFM Skorlama:** Müşteriler; Yenilik (**R**ecency), Sıklık (**F**requency) ve Parasal Değer (**M**onetary) kriterlerine göre puanlanmıştır.
* **3D Kümeleme (Clustering):** **K-Means** makine öğrenmesi algoritması kullanılarak müşteriler 3 boyutlu bir uzayda segmentlere ayrılmıştır.
* **İnteraktif Dashboard:** **Flask** ve **Plotly** kullanılarak hazırlanan web arayüzü sayesinde veriler canlı olarak görselleştirilmiştir.

## 🛠️ Teknik Altyapı
* **Dil:** Python
* **Web Framework:** Flask
* **Veri Analizi:** Pandas, NumPy
* **Makine Öğrenmesi:** Scikit-Learn (K-Means)
* **Görselleştirme:** Plotly

## 🚀 Kurulum ve Çalıştırma
1. Projeyi klonlayın: `git clone https://github.com/ebruboztas/data-analysis-challenge.git`
2. Gerekli kütüphaneleri kurun: `pip install flask pandas plotly scikit-learn openpyxl`
3. Uygulamayı başlatın: `python app.py`
4. Tarayıcınızdan `http://127.0.0.1:5000` adresine gidin.

---
**Hazırlayan:** Ebru Boztaş


