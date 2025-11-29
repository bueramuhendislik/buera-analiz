import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

# --- MARKA RENKLERİ ---
BRAND_NAVY = '#0F172A'
BRAND_ORANGE = '#F59E0B'
BRAND_WHITE = '#F8FAFC'

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="BUERA | Mühendislik Analiz Sistemi",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZORUNLU CSS (MARKALAŞTIRMA) ---
# Bu kısım, uygulamanın arka planını lacivert, yazıları beyaz yapar.
st.markdown(f"""
<style>
    /* Ana arka plan */
    .stApp {{
        background-color: {BRAND_NAVY};
        color: {BRAND_WHITE};
    }}
    /* Yan menü arka planı */
    [data-testid="stSidebar"] {{
        background-color: #1E293B; /* Biraz daha açık lacivert tonu */
    }}
    /* Tüm yazıları beyaz yap */
    h1, h2, h3, h4, h5, h6, p, span, div, label {{
        color: {BRAND_WHITE} !important;
    }}
    /* Metrik değerlerini turuncu yap */
    [data-testid="stMetricValue"] {{
        color: {BRAND_ORANGE} !important;
    }}
    /* Slider renkleri */
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{{
        background-color: {BRAND_ORANGE};
    }}
    .stSlider div[data-testid="stMarkdownContainer"] p {{
       color: {BRAND_WHITE} !important;
    }}
</style>
""", unsafe_allow_html=True)

# --- LOGO ALANI ---
# Klasöründeki 'logo.png' dosyasını burada gösteriyoruz.
try:
    image = Image.open('logo.png')
    st.image(image, width=250) # Genişliği ayarlayabilirsin
except FileNotFoundError:
    st.warning("⚠️ 'logo.png' dosyası bulunamadı. Lütfen proje klasörüne logonuzu ekleyin.")
    st.title("BUERA MÜHENDİSLİK") # Logo yoksa yazı yazar

st.markdown(f"<h3 style='color:{BRAND_ORANGE};'>Veri Odaklı İşletme Analiz Kokpiti</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ (KİMLİK) ---
st.sidebar.header("📋 İşletme Kimliği")
isletme_adi = st.sidebar.text_input("İşletme Adı", "Örnek İşletme A.Ş.")
yetkili = st.sidebar.text_input("Yetkili Kişi", "Ad Soyad")
sektor = st.sidebar.selectbox("Sektör Seçimi", ["Perakende (Telefon/Kırtasiye)", "Hizmet (Berber/Güzellik)", "Yeme-İçme (Kafe/Restoran)"])

st.sidebar.markdown("---")
st.sidebar.info("Bu analiz, BUERA Endüstri Mühendisliği algoritmalarıyla hesaplanmaktadır.")
st.sidebar.caption("© 2024 BUERA Engineering")

# --- ANALİZ MOTORU ---
st.header(f"📊 {isletme_adi} | {sektor} Analizi")

scores = {}
col1, col2 = st.columns(2)

# Sektöre Göre Sorular (10 Maddelik Tam Kapsam)
if sektor == "Perakende (Telefon/Kırtasiye)":
    with col1:
        st.subheader("🏭 Operasyonel Süreçler")
        scores['Stok Yönetimi (ABC)'] = st.slider("Stok Doğruluğu ve Ölü Stok Takibi", 0, 10, 5)
        scores['Raf Düzeni (Layout)'] = st.slider("Ürün Yerleşimi ve Görünürlük", 0, 10, 5)
        scores['Depo Düzeni (5S)'] = st.slider("Depo Tertip ve Düzeni", 0, 10, 5)
        scores['Tedarik Hızı'] = st.slider("Eksik Ürün Tamamlama Hızı", 0, 10, 5)
        scores['Hata Önleme'] = st.slider("Barkod/Etiket Hataları", 0, 10, 5)
    with col2:
        st.subheader("🚀 Satış & Dijital")
        scores['Çapraz Satış'] = st.slider("Kasa Önü Ek Satış Başarısı", 0, 10, 5)
        scores['Müşteri Deneyimi'] = st.slider("Mağaza İçi Müşteri Memnuniyeti", 0, 10, 5)
        scores['Google Haritalar'] = st.slider("Google Puanı ve Yorumlar", 0, 10, 5)
        scores['Instagram Vitrini'] = st.slider("Sosyal Medya Görsel Kalitesi", 0, 10, 5)
        scores['Rakip Analizi'] = st.slider("Rakiplere Göre Fiyat/Hizmet Durumu", 0, 10, 5)

elif sektor == "Hizmet (Berber/Güzellik)":
    with col1:
        st.subheader("⏳ Zaman & Kapasite")
        scores['İşlem Hızı'] = st.slider("Standart Hizmet Süresi (Hız)", 0, 10, 5)
        scores['Randevu Sistemi'] = st.slider("Randevu Sadakati ve Çakışma", 0, 10, 5)
        scores['Kapasite Kullanımı'] = st.slider("Koltuk Doluluk Oranı (Ölü Saatler)", 0, 10, 5)
        scores['Hazırlık Süresi'] = st.slider("Müşteri Arası Temizlik Süresi", 0, 10, 5)
        scores['Ergonomi'] = st.slider("Çalışma Alanı Düzeni", 0, 10, 5)
    with col2:
        st.subheader("💎 Müşteri & Marka")
        scores['Müşteri Sadakati'] = st.slider("Tekrar Gelen Müşteri Oranı", 0, 10, 5)
        scores['Hizmet Kalitesi'] = st.slider("Müşteri Memnuniyet Seviyesi", 0, 10, 5)
        scores['Google Yorumlar'] = st.slider("Harita Puanı ve Yorum Cevaplama", 0, 10, 5)
        scores['Instagram Reels'] = st.slider("Video İçerik Üretim Sıklığı", 0, 10, 5)
        scores['Marka İmajı'] = st.slider("Dükkanın Genel Kurumsal Havası", 0, 10, 5)

elif sektor == "Yeme-İçme (Kafe/Restoran)":
    with col1:
        st.subheader("🍳 Mutfak & Operasyon")
        scores['Menü Mühendisliği'] = st.slider("Menü Kârlılık Analizi (Yıldız/Dog)", 0, 10, 5)
        scores['Servis Hızı'] = st.slider("Siparişten Teslime Geçen Süre", 0, 10, 5)
        scores['Mutfak Akışı'] = st.slider("Mutfak Düzeni ve Gereksiz Hareket", 0, 10, 5)
        scores['Atık Yönetimi'] = st.slider("Gıda İsrafı Oranı", 0, 10, 5)
        scores['Hijyen (5S)'] = st.slider("Genel Temizlik ve Düzen", 0, 10, 5)
    with col2:
        st.subheader("📈 Satış & Yönetim")
        scores['Masa Devir Hızı'] = st.slider("Masa Sirkülasyonu", 0, 10, 5)
        scores['Stok (FIFO)'] = st.slider("SKT Takibi ve Depo Düzeni", 0, 10, 5)
        scores['Standart Reçete'] = st.slider("Gramaj ve Lezzet Standartı", 0, 10, 5)
        scores['Dijital Menü/Sipariş'] = st.slider("Online Varlık ve QR Menü", 0, 10, 5)
        scores['Müşteri Yorumları'] = st.slider("Yemek Sepeti/Google Puanı", 0, 10, 5)

# --- GRAFİK (RADAR CHART - MARKAYA ÖZEL) ---
st.markdown("---")
col_graph, col_result = st.columns([1.5, 1])

with col_graph:
    st.subheader("🕸️ Performans Radarı")
    categories = list(scores.keys())
    values = list(scores.values())

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=isletme_adi,
        line_color=BRAND_ORANGE, # Çizgi rengi TURUNCU
        fillcolor=f'rgba(245, 158, 11, 0.3)', # Dolgu rengi şeffaf turuncu
        marker=dict(color=BRAND_ORANGE)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(color=BRAND_WHITE), gridcolor='#334155'),
            angularaxis=dict(tickfont=dict(color=BRAND_WHITE), gridcolor='#334155'),
            bgcolor=BRAND_NAVY # Grafik zemini lacivert
        ),
        paper_bgcolor=BRAND_NAVY, # Tüm kağıt zemini lacivert
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- SONUÇ ALANI ---
with col_result:
    st.subheader("🏆 Analiz Sonucu")
    ortalama_puan = sum(values) / len(values)

    # Skoru Turuncu renkte göster
    st.metric(label="GENEL BUERA SKORU", value=f"{ortalama_puan:.1f} / 10")

    if ortalama_puan >= 8:
        st.success("DURUM: MÜKEMMEL 🌟 (Strateji: Koruma ve mikro iyileştirme)")
    elif 6 <= ortalama_puan < 8:
        st.warning("DURUM: İYİ AMA RİSKLİ ⚠️ (Strateji: Zayıf noktalara odaklanma)")
    else:
        st.error("DURUM: KRİTİK 🚨 (Strateji: Acil müdahale planı)")

    st.markdown("---")
    st.markdown("### 💊 Mühendislik Reçetesi")
    
    zayif_noktalar = {k: v for k, v in scores.items() if v < 6}
    guclu_noktalar = {k: v for k, v in scores.items() if v >= 9}

    if not zayif_noktalar:
        st.write("✅ Kritik bir zayıf nokta tespit edilemedi.")
    else:
        st.write("Acil İyileştirme Gereken Alanlar:")
        for key, value in zayif_noktalar.items():
             st.markdown(f"- ❌ **{key} ({value}/10)**")
             
    if guclu_noktalar:
        st.markdown("---")
        st.write("Korunması Gereken Güçlü Alanlar:")
        for key, value in guclu_noktalar.items():
             st.markdown(f"- ⭐ **{key} ({value}/10)**")