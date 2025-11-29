import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

# --- MARKA RENKLERİ ---
BRAND_NAVY = '#0F172A'
BRAND_ORANGE = '#F59E0B'
BRAND_WHITE = '#F8FAFC'
BRAND_INPUT_BG = '#1E293B'

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="BUERA | Mühendislik Analiz Sistemi",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZORUNLU CSS (BEYAZLIKLARI YOK EDEN VERSİYON) ---
st.markdown(f"""
<style>
    /* Ana arka plan */
    .stApp {{
        background-color: {BRAND_NAVY};
        color: {BRAND_WHITE};
    }}
    /* Yan menü arka planı */
    [data-testid="stSidebar"] {{
        background-color: {BRAND_INPUT_BG};
    }}
    /* Tüm genel yazıları beyaz yap */
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {{
        color: {BRAND_WHITE} !important;
    }}
    /* Metrik değerlerini turuncu yap */
    [data-testid="stMetricValue"] {{
        color: {BRAND_ORANGE} !important;
    }}
    
    /* --- GİRİŞ KUTULARI --- */
    [data-testid="stTextInput"] input {{
        background-color: {BRAND_INPUT_BG} !important;
        color: {BRAND_WHITE} !important;
        border: 1px solid {BRAND_ORANGE} !important;
    }}
    
    /* --- SEÇİM KUTULARI --- */
    div[data-baseweb="select"] > div {{
        background-color: {BRAND_INPUT_BG} !important;
        color: {BRAND_WHITE} !important;
        border: 1px solid {BRAND_ORANGE} !important;
    }}
    div[data-baseweb="popover"] div {{
        background-color: {BRAND_INPUT_BG} !important;
        color: {BRAND_WHITE} !important;
    }}
    
    /* --- RAPOR KUTUSU (ST.CODE) KESİN DÜZELTME --- */
    /* Kutunun içindeki HER ŞEYİ zorla koyu yap */
    [data-testid="stCodeBlock"] {{
        background-color: {BRAND_INPUT_BG} !important;
        border: 1px solid {BRAND_ORANGE} !important;
        border-radius: 10px !important;
    }}
    [data-testid="stCodeBlock"] * {{
        background-color: {BRAND_INPUT_BG} !important;
        color: {BRAND_WHITE} !important;
        font-family: 'Source Code Pro', monospace !important;
    }}
    
    /* Kopyala butonu özel ayarı */
    [data-testid="stCodeBlock"] button {{
        background-color: transparent !important;
        color: {BRAND_WHITE} !important;
    }}
    [data-testid="stCodeBlock"] button:hover {{
        color: {BRAND_ORANGE} !important;
    }}
    
    /* --- SLIDER RENKLERİ --- */
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{{
        background-color: {BRAND_ORANGE};
    }}
    .streamlit-expanderHeader {{ color: {BRAND_ORANGE} !important; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)

# --- LOGO ALANI ---
try:
    try:
        image = Image.open('logo.png')
    except:
        image = Image.open('logo.jpg')
    st.image(image, width=200)
except:
    st.title("BUERA")

st.markdown(f"<h3 style='color:{BRAND_ORANGE};'>Veri Odaklı İşletme Analiz Kokpiti</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ ---
st.sidebar.header("📋 İşletme Kimliği")
isletme_adi = st.sidebar.text_input("İşletme Adı", "Örnek İşletme")
yetkili = st.sidebar.text_input("Yetkili Kişi", "Ad Soyad")
sektor = st.sidebar.selectbox("Sektör Seçimi", [
    "Perakende (Telefon/Kırtasiye/Butik)", 
    "Hizmet (Berber/Güzellik/Klinik)", 
    "Yeme-İçme (Kafe/Restoran)", 
    "Market & Süpermarket",
    "Spor Salonu & Gym",
    "Oto Servis & Sanayi",
    "Emlak & Danışmanlık",
    "E-Ticaret & Online Satış"
])

st.sidebar.markdown("---")
st.sidebar.info("Bu analiz, BUERA Endüstri Mühendisliği algoritmalarıyla hesaplanmaktadır.")
st.sidebar.caption("© 2024 BUERA Engineering")

# --- ANALİZ MOTORU ---
st.header(f"📊 {isletme_adi} | {sektor} Analizi")

# --- PUANLAMA REHBERİ ---
def puanlama_rehberi_goster():
    with st.expander("ℹ️ PUANLAMA REHBERİ (Nasıl Puanlamalıyım?)"):
        st.markdown("""
        **1 - 3 Puan (Kritik):** Süreç yok, her şey manuel, hatalar sık, ölçüm yok.
        **4 - 7 Puan (Orta):** Kısmi düzen var ama standartlaşmamış, bazen aksıyor.
        **8 - 10 Puan (Mükemmel):** Yazılımlar kullanılıyor, hata sıfıra yakın, tam otomatik.
        """)

puanlama_rehberi_goster()

scores = {}
col1, col2 = st.columns(2)

# --- SORU HAVUZU (8 SEKTÖR) ---

# 1. PERAKENDE
if "Perakende" in sektor:
    with col1:
        st.subheader("🏭 Operasyonel Süreçler")
        scores['Stok Yönetimi (ABC)'] = st.slider("Stok Doğruluğu", 0, 10, 5)
        scores['Raf Düzeni'] = st.slider("Ürün Yerleşimi (Planogram)", 0, 10, 5)
        scores['Depo Düzeni (5S)'] = st.slider("Depo Tertip ve Düzeni", 0, 10, 5)
        scores['Tedarik Hızı'] = st.slider("Eksik Ürün Tamamlama", 0, 10, 5)
        scores['Hata Önleme'] = st.slider("Barkod/Etiket Hataları", 0, 10, 5)
    with col2:
        st.subheader("🚀 Satış & Dijital")
        scores['Çapraz Satış'] = st.slider("Kasa Önü Ek Satış", 0, 10, 5)
        scores['Müşteri Deneyimi'] = st.slider("Mağaza İçi İlgi", 0, 10, 5)
        scores['Google Haritalar'] = st.slider("Google Puanı", 0, 10, 5)
        scores['Instagram Vitrini'] = st.slider("Sosyal Medya Kalitesi", 0, 10, 5)
        scores['Rakip Analizi'] = st.slider("Fiyat Rekabeti", 0, 10, 5)

# 2. HİZMET
elif "Hizmet" in sektor:
    with col1:
        st.subheader("⏳ Zaman & Kapasite")
        scores['İşlem Hızı'] = st.slider("Standart İşlem Süresi", 0, 10, 5)
        scores['Randevu Sistemi'] = st.slider("Randevu Sadakati", 0, 10, 5)
        scores['Kapasite Kullanımı'] = st.slider("Koltuk Doluluk Oranı", 0, 10, 5)
        scores['Hazırlık Süresi'] = st.slider("Hijyen Hazırlık Hızı", 0, 10, 5)
        scores['Ergonomi'] = st.slider("Çalışma Alanı Düzeni", 0, 10, 5)
    with col2:
        st.subheader("💎 Marka & Deneyim")
        scores['Müşteri Sadakati'] = st.slider("Tekrar Gelen Müşteri", 0, 10, 5)
        scores['Hizmet Kalitesi'] = st.slider("Müşteri Memnuniyeti", 0, 10, 5)
        scores['Google Yorumlar'] = st.slider("Harita Puanı", 0, 10, 5)
        scores['Video İçerik'] = st.slider("Reels Paylaşımı", 0, 10, 5)
        scores['Kurumsal İmaj'] = st.slider("Salon Atmosferi", 0, 10, 5)

# 3. YEME-İÇME
elif "Yeme-İçme" in sektor:
    with col1:
        st.subheader("🍳 Mutfak & Operasyon")
        scores['Menü Müh.'] = st.slider("Menü Kârlılığı", 0, 10, 5)
        scores['Servis Hızı'] = st.slider("Sipariş Süresi", 0, 10, 5)
        scores['Mutfak Akışı'] = st.slider("Mutfak Düzeni", 0, 10, 5)
        scores['Atık Yönetimi'] = st.slider("Gıda İsrafı", 0, 10, 5)
        scores['Hijyen (5S)'] = st.slider("Temizlik Standartları", 0, 10, 5)
    with col2:
        st.subheader("📈 Satış & Yönetim")
        scores['Masa Devri'] = st.slider("Sirkülasyon", 0, 10, 5)
        scores['Stok (FIFO)'] = st.slider("Depo Yönetimi", 0, 10, 5)
        scores['Standart Reçete'] = st.slider("Lezzet Standardı", 0, 10, 5)
        scores['Dijital Menü'] = st.slider("QR ve Online Varlık", 0, 10, 5)
        scores['Puan Durumu'] = st.slider("Platform Puanları", 0, 10, 5)

# 4. MARKET
elif "Market" in sektor:
    with col1:
        st.subheader("🛒 Market Operasyonları")
        scores['Raf Bulunurluğu'] = st.slider("Raf Doluluk Oranı", 0, 10, 5)
        scores['SKT Yönetimi'] = st.slider("Son Kullanma Takibi", 0, 10, 5)
        scores['Kasa Kuyruğu'] = st.slider("Kasa İşlem Hızı", 0, 10, 5)
        scores['Depo Düzeni'] = st.slider("Depo ve İstifleme", 0, 10, 5)
        scores['Temizlik'] = st.slider("Mağaza Temizliği", 0, 10, 5)
    with col2:
        st.subheader("📣 Pazarlama & Yerel")
        scores['İndirim/Insert'] = st.slider("Kampanya Yönetimi", 0, 10, 5)
        scores['Müşteri Sadakati'] = st.slider("Sadık Müşteri Kartı", 0, 10, 5)
        scores['Google Harita'] = st.slider("Yerel Görünürlük", 0, 10, 5)
        scores['Sosyal Medya'] = st.slider("Ürün Paylaşımları", 0, 10, 5)
        scores['Sepet Büyüklüğü'] = st.slider("Ortalama Sepet Tutarı", 0, 10, 5)

# 5. SPOR SALONU
elif "Spor Salonu" in sektor:
    with col1:
        st.subheader("💪 Salon Verimliliği")
        scores['Ekipman Bakımı'] = st.slider("Aletlerin Durumu", 0, 10, 5)
        scores['Kapasite (Pik)'] = st.slider("Yoğun Saat Yönetimi", 0, 10, 5)
        scores['Hijyen/Havalandırma'] = st.slider("Temizlik ve Koku", 0, 10, 5)
        scores['Enerji Tasarrufu'] = st.slider("Elektrik/Su Gideri", 0, 10, 5)
        scores['Personel Takibi'] = st.slider("Antrenör İlgisi", 0, 10, 5)
    with col2:
        st.subheader("🔥 Üye & Pazarlama")
        scores['Üye Devamlılığı'] = st.slider("Retention (Sadakat)", 0, 10, 5)
        scores['Dönüşüm Hikayeleri'] = st.slider("Before/After Paylaşımı", 0, 10, 5)
        scores['Google Yorumlar'] = st.slider("Salon Puanı", 0, 10, 5)
        scores['Instagram Etkileşimi'] = st.slider("Motivasyon İçerikleri", 0, 10, 5)
        scores['Kampanya Kurgusu'] = st.slider("Yeni Üye Kazanımı", 0, 10, 5)

# 6. OTO SERVİS
elif "Oto Servis" in sektor:
    with col1:
        st.subheader("🔧 Servis Operasyonu")
        scores['Arıza Tespit'] = st.slider("Teşhis Doğruluğu/Hızı", 0, 10, 5)
        scores['Parça Tedariği'] = st.slider("Yedek Parça Lojistiği", 0, 10, 5)
        scores['Lift Kullanımı'] = st.slider("Lift/Kanal Doluluğu", 0, 10, 5)
        scores['Takım Düzeni'] = st.slider("5S (Takımhane)", 0, 10, 5)
        scores['Teslimat Süresi'] = st.slider("Söz Verilen Süre", 0, 10, 5)
    with col2:
        st.subheader("🤝 Müşteri & Güven")
        scores['Güvenilirlik'] = st.slider("Müşteri Güveni", 0, 10, 5)
        scores['Randevu Sistemi'] = st.slider("İş Kabul Düzeni", 0, 10, 5)
        scores['Google Harita'] = st.slider("Yorum ve Puanlar", 0, 10, 5)
        scores['Bilgilendirme'] = st.slider("Süreç Bilgilendirmesi", 0, 10, 5)
        scores['Kurumsallık'] = st.slider("Bekleme Alanı/Giyim", 0, 10, 5)

# 7. EMLAK
elif "Emlak" in sektor:
    with col1:
        st.subheader("🏠 Portföy Yönetimi")
        scores['Portföy Genişliği'] = st.slider("İlan Sayısı", 0, 10, 5)
        scores['Dönüş Hızı'] = st.slider("Müşteriye Dönüş", 0, 10, 5)
        scores['Veri Tabanı'] = st.slider("CRM / Müşteri Kaydı", 0, 10, 5)
        scores['Sözleşme Düzeni'] = st.slider("Resmi Evrak Takibi", 0, 10, 5)
        scores['Bölge Hakimiyeti'] = st.slider("Fiyat Analizi", 0, 10, 5)
    with col2:
        st.subheader("📢 Dijital Pazarlama")
        scores['İlan Kalitesi'] = st.slider("Fotoğraf/Video Çekimi", 0, 10, 5)
        scores['Sahibinden/Portal'] = st.slider("İlan Açıklamaları", 0, 10, 5)
        scores['Kişisel Marka'] = st.slider("Sosyal Medya Duruşu", 0, 10, 5)
        scores['Video Tur'] = st.slider("Ev Tanıtım Videoları", 0, 10, 5)
        scores['Referanslar'] = st.slider("Mutlu Müşteriler", 0, 10, 5)

# 8. E-TİCARET
elif "E-Ticaret" in sektor:
    with col1:
        st.subheader("📦 Lojistik & Depo")
        scores['Kargolama Hızı'] = st.slider("Siparişten Kargoya Süre", 0, 10, 5)
        scores['Stok Takibi'] = st.slider("Entegrasyon Doğruluğu", 0, 10, 5)
        scores['Paketleme'] = st.slider("Paket Kalitesi", 0, 10, 5)
        scores['İade Yönetimi'] = st.slider("İade Oranı", 0, 10, 5)
        scores['Maliyet Analizi'] = st.slider("Kârlılık Hesabı", 0, 10, 5)
    with col2:
        st.subheader("💻 Dijital Pazarlama")
        scores['Fotoğraf Kalitesi'] = st.slider("Ürün Görselleri", 0, 10, 5)
        scores['Reklam (ROAS)'] = st.slider("Reklam Performansı", 0, 10, 5)
        scores['Sosyal Medya'] = st.slider("Instagram/TikTok", 0, 10, 5)
        scores['Müşteri Yorumları'] = st.slider("Mağaza Puanı", 0, 10, 5)
        scores['Kampanya'] = st.slider("Sepet Ortalaması", 0, 10, 5)

# --- GRAFİK ---
st.markdown("---")
col_graph, col_result = st.columns([1.5, 1])

# Hesaplamaları burada yapıyoruz
ortalama_puan = sum(values := list(scores.values())) / len(values) if scores else 0
zayif_noktalar = {k: v for k, v in scores.items() if v < 6}

with col_graph:
    st.subheader("🕸️ Performans Radarı")
    if scores:
        categories = list(scores.keys())
        values = list(scores.values())
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values, theta=categories, fill='toself', name=isletme_adi,
            line_color=BRAND_ORANGE, fillcolor=f'rgba(245, 158, 11, 0.3)', marker=dict(color=BRAND_ORANGE)
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(color=BRAND_WHITE), gridcolor='#334155'),
                angularaxis=dict(tickfont=dict(color=BRAND_WHITE), gridcolor='#334155'),
                bgcolor=BRAND_NAVY
            ),
            paper_bgcolor=BRAND_NAVY, showlegend=False, margin=dict(l=40, r=40, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)

# --- SONUÇ ---
with col_result:
    st.subheader("🏆 Analiz Sonucu")
    st.metric(label="GENEL BUERA SKORU", value=f"{ortalama_puan:.1f} / 10")

    if ortalama_puan >= 8:
        st.success("DURUM: MÜKEMMEL 🌟")
        st.write("İşletme çok iyi durumda. Strateji: Koruma ve mikro iyileştirmeler.")
    elif 6 <= ortalama_puan < 8:
        st.warning("DURUM: İYİ AMA RİSKLİ ⚠️")
        st.write("Kritik süreçlerde iyileştirme yapılırsa ciro %30 artabilir.")
    else:
        st.error("DURUM: KRİTİK 🚨")
        st.write("Acil müdahale gerekli! Ciddi verimlilik ve müşteri kaybı var.")

    st.markdown("---")
    with st.expander("💊 MÜHENDİSLİK REÇETESİ", expanded=True):
        if not zayif_noktalar: st.write("✅ Kritik zayıf nokta yok.")
        else:
            for k, v in zayif_noktalar.items(): st.markdown(f"- ❌ **{k} ({v}/10):** İyileştirilmeli.")

# --- INSTAGRAM RAPOR GÖNDERME ---
st.markdown("---")
st.subheader("🚀 SONUÇLARI BİZE İLETİN")
st.info("Bu analizi uzman ekibimizle paylaşarak işletmenize özel ücretsiz yol haritasını alın.")

rapor_metni = f"""
Merhaba BUERA,
İşletme Analiz Sonuçlarım:

📋 İşletme: {isletme_adi} ({yetkili})
🏭 Sektör: {sektor}
🏆 BUPROM Skorum: {ortalama_puan:.1f} / 10

🔻 Zayıf Noktalarım:
{', '.join([f"{k} ({v})" for k, v in zayif_noktalar.items()])}

Bu konuda destek almak istiyorum.
"""

st.markdown("##### 1️⃣ Aşağıdaki Raporu Kopyalayın:")
st.code(rapor_metni, language="text")

st.markdown("##### 2️⃣ Instagram'dan Bize Gönderin:")
instagram_link = "https://ig.me/m/bueramuhendislik"

st.markdown(f"""
<a href="{instagram_link}" target="_blank">
    <button style="
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color:white; border:none; padding:15px 32px; text-align:center; text-decoration:none; 
        display:inline-block; font-size:16px; font-weight:bold; border-radius:10px; cursor:pointer; width:100%;">
        📸 INSTAGRAM DM İLE GÖNDER
    </button>
</a>
""", unsafe_allow_html=True)