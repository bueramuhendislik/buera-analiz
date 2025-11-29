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

# --- ZORUNLU CSS ---
st.markdown(f"""
<style>
    .stApp {{ background-color: {BRAND_NAVY}; color: {BRAND_WHITE}; }}
    [data-testid="stSidebar"] {{ background-color: #1E293B; }}
    h1, h2, h3, h4, h5, h6, p, span, div, label {{ color: {BRAND_WHITE} !important; }}
    [data-testid="stMetricValue"] {{ color: {BRAND_ORANGE} !important; }}
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{{ background-color: {BRAND_ORANGE}; }}
    .stSlider div[data-testid="stMarkdownContainer"] p {{ color: {BRAND_WHITE} !important; }}
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
# SEKTÖR LİSTESİ GENİŞLETİLDİ (8 SEKTÖR)
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

# --- SORU HAVUZU (SEKTÖRE GÖRE DEĞİŞEN ALGORİTMA) ---

# 1. PERAKENDE
if "Perakende" in sektor:
    with col1:
        st.subheader("🏭 Operasyonel Süreçler")
        scores['Stok Yönetimi (ABC)'] = st.slider("Stok Doğruluğu", 0, 10, 5, help="Ölü stok takibi ve sayım doğruluğu")
        scores['Raf Düzeni'] = st.slider("Ürün Yerleşimi (Planogram)", 0, 10, 5, help="En çok satanlar göz hizasında mı?")
        scores['Depo Düzeni (5S)'] = st.slider("Depo Tertip ve Düzeni", 0, 10, 5, help="Aranan ürün saniyeler içinde bulunuyor mu?")
        scores['Tedarik Hızı'] = st.slider("Eksik Ürün Tamamlama", 0, 10, 5, help="Ürün bitmeden sipariş geçiliyor mu?")
        scores['Hata Önleme'] = st.slider("Barkod/Etiket Hataları", 0, 10, 5, help="Etiket ve kasa fiyatı tutuyor mu?")
    with col2:
        st.subheader("🚀 Satış & Dijital")
        scores['Çapraz Satış'] = st.slider("Kasa Önü Ek Satış", 0, 10, 5, help="Müşteriye ek ürün teklif ediliyor mu?")
        scores['Müşteri Deneyimi'] = st.slider("Mağaza İçi İlgi", 0, 10, 5, help="Personel ilgisi ve karşılama")
        scores['Google Haritalar'] = st.slider("Google Puanı", 0, 10, 5, help="Harita yorumları ve puanı")
        scores['Instagram Vitrini'] = st.slider("Sosyal Medya Kalitesi", 0, 10, 5, help="Ürün fotoğrafları ve Reels kalitesi")
        scores['Rakip Analizi'] = st.slider("Fiyat Rekabeti", 0, 10, 5, help="Rakiplerin fiyatları takip ediliyor mu?")

# 2. HİZMET (BERBER/GÜZELLİK)
elif "Hizmet" in sektor:
    with col1:
        st.subheader("⏳ Zaman & Kapasite")
        scores['İşlem Hızı'] = st.slider("Standart İşlem Süresi", 0, 10, 5, help="İşlemler standart sürede bitiyor mu?")
        scores['Randevu Sistemi'] = st.slider("Randevu Sadakati", 0, 10, 5, help="Çakışma veya bekletme oluyor mu?")
        scores['Kapasite Kullanımı'] = st.slider("Koltuk Doluluk Oranı", 0, 10, 5, help="Boş saatler değerlendiriliyor mu?")
        scores['Hazırlık Süresi'] = st.slider("Hijyen Hazırlık Hızı", 0, 10, 5, help="Müşteri arası temizlik süresi")
        scores['Ergonomi'] = st.slider("Çalışma Alanı Düzeni", 0, 10, 5, help="Malzemeler el altında mı?")
    with col2:
        st.subheader("💎 Marka & Deneyim")
        scores['Müşteri Sadakati'] = st.slider("Tekrar Gelen Müşteri", 0, 10, 5, help="Müşteri geri dönüş oranı (Retention)")
        scores['Hizmet Kalitesi'] = st.slider("Müşteri Memnuniyeti", 0, 10, 5, help="İşlem sonrası memnuniyet")
        scores['Google Yorumlar'] = st.slider("Harita Puanı", 0, 10, 5, help="Yorumlara cevap veriliyor mu?")
        scores['Video İçerik'] = st.slider("Reels Paylaşımı", 0, 10, 5, help="Yapılan işlerin videoları çekiliyor mu?")
        scores['Kurumsal İmaj'] = st.slider("Salon Atmosferi", 0, 10, 5, help="Müzik, koku ve genel hava")

# 3. YEME-İÇME
elif "Yeme-İçme" in sektor:
    with col1:
        st.subheader("🍳 Mutfak & Operasyon")
        scores['Menü Müh.'] = st.slider("Menü Kârlılığı", 0, 10, 5, help="Hangi ürün kârlı, hangisi zararlı biliniyor mu?")
        scores['Servis Hızı'] = st.slider("Sipariş Süresi", 0, 10, 5, help="Müşteri bekleme süresi")
        scores['Mutfak Akışı'] = st.slider("Mutfak Düzeni", 0, 10, 5, help="Çalışanlar birbirine çarpıyor mu?")
        scores['Atık Yönetimi'] = st.slider("Gıda İsrafı", 0, 10, 5, help="Çöpe giden yemek oranı")
        scores['Hijyen (5S)'] = st.slider("Temizlik Standartları", 0, 10, 5, help="Mutfak ve WC temizliği")
    with col2:
        st.subheader("📈 Satış & Yönetim")
        scores['Masa Devri'] = st.slider("Sirkülasyon", 0, 10, 5, help="Masalar ne kadar hızlı dolup boşalıyor?")
        scores['Stok (FIFO)'] = st.slider("Depo Yönetimi", 0, 10, 5, help="SKT takibi yapılıyor mu?")
        scores['Standart Reçete'] = st.slider("Lezzet Standardı", 0, 10, 5, help="Her gün aynı lezzet çıkıyor mu?")
        scores['Dijital Menü'] = st.slider("QR ve Online Varlık", 0, 10, 5, help="QR menü veya online sipariş var mı?")
        scores['Puan Durumu'] = st.slider("Platform Puanları", 0, 10, 5, help="Yemeksepeti/Google puanları")

# 4. MARKET & SÜPERMARKET
elif "Market" in sektor:
    with col1:
        st.subheader("🛒 Market Operasyonları")
        scores['Raf Bulunurluğu'] = st.slider("Raf Doluluk Oranı", 0, 10, 5, help="Raflar boş kalıyor mu?")
        scores['SKT Yönetimi'] = st.slider("Son Kullanma Takibi", 0, 10, 5, help="Tarihi geçen ürünler rafta kalıyor mu?")
        scores['Kasa Kuyruğu'] = st.slider("Kasa İşlem Hızı", 0, 10, 5, help="Müşteriler kuyrukta bekliyor mu?")
        scores['Depo Düzeni'] = st.slider("Depo ve İstifleme", 0, 10, 5, help="Depodan mal çıkarmak ne kadar sürüyor?")
        scores['Temizlik'] = st.slider("Mağaza Temizliği", 0, 10, 5, help="Zemin ve raf temizliği")
    with col2:
        st.subheader("📣 Pazarlama & Yerel")
        scores['İndirim/Insert'] = st.slider("Kampanya Yönetimi", 0, 10, 5, help="Haftalık indirimler duyuruluyor mu?")
        scores['Müşteri Sadakati'] = st.slider("Sadık Müşteri Kartı", 0, 10, 5, help="Veresiye veya sadakat kartı sistemi")
        scores['Google Harita'] = st.slider("Yerel Görünürlük", 0, 10, 5, help="Haritada kolay bulunuyor mu?")
        scores['Sosyal Medya'] = st.slider("Ürün Paylaşımları", 0, 10, 5, help="Yeni gelen ürünler paylaşılıyor mu?")
        scores['Sepet Büyüklüğü'] = st.slider("Ortalama Sepet Tutarı", 0, 10, 5, help="Müşteriler az mı çok mu alıyor?")

# 5. SPOR SALONU & GYM
elif "Spor Salonu" in sektor:
    with col1:
        st.subheader("💪 Salon Verimliliği")
        scores['Ekipman Bakımı'] = st.slider("Aletlerin Durumu", 0, 10, 5, help="Bozuk alet var mı?")
        scores['Kapasite (Pik)'] = st.slider("Yoğun Saat Yönetimi", 0, 10, 5, help="Akşam saatlerinde yığılma oluyor mu?")
        scores['Hijyen/Havalandırma'] = st.slider("Temizlik ve Koku", 0, 10, 5, help="Salon temiz kokuyor mu?")
        scores['Enerji Tasarrufu'] = st.slider("Elektrik/Su Gideri", 0, 10, 5, help="Gereksiz yanan ışıklar/klimalar")
        scores['Personel Takibi'] = st.slider("Antrenör İlgisi", 0, 10, 5, help="Hocalar üyelerle ilgileniyor mu?")
    with col2:
        st.subheader("🔥 Üye & Pazarlama")
        scores['Üye Devamlılığı'] = st.slider("Retention (Sadakat)", 0, 10, 5, help="Üyeler yenileme yapıyor mu?")
        scores['Dönüşüm Hikayeleri'] = st.slider("Before/After Paylaşımı", 0, 10, 5, help="Üye gelişimleri paylaşılıyor mu?")
        scores['Google Yorumlar'] = st.slider("Salon Puanı", 0, 10, 5, help="Google puanı kaç?")
        scores['Instagram Etkileşimi'] = st.slider("Motivasyon İçerikleri", 0, 10, 5, help="Spor videoları paylaşılıyor mu?")
        scores['Kampanya Kurgusu'] = st.slider("Yeni Üye Kazanımı", 0, 10, 5, help="Dönemsel kampanyalar yapılıyor mu?")

# 6. OTO SERVİS & SANAYİ
elif "Oto Servis" in sektor:
    with col1:
        st.subheader("🔧 Servis Operasyonu")
        scores['Arıza Tespit'] = st.slider("Teşhis Doğruluğu/Hızı", 0, 10, 5, help="Arıza tek seferde bulunuyor mu?")
        scores['Parça Tedariği'] = st.slider("Yedek Parça Lojistiği", 0, 10, 5, help="Parça beklerken araç yatıyor mu?")
        scores['Lift Kullanımı'] = st.slider("Lift/Kanal Doluluğu", 0, 10, 5, help="Çalışma alanları verimli kullanılıyor mu?")
        scores['Takım Düzeni'] = st.slider("5S (Takımhane)", 0, 10, 5, help="Anahtarlar yerli yerinde mi?")
        scores['Teslimat Süresi'] = st.slider("Söz Verilen Süre", 0, 10, 5, help="Araç zamanında teslim ediliyor mu?")
    with col2:
        st.subheader("🤝 Müşteri & Güven")
        scores['Güvenilirlik'] = st.slider("Müşteri Güveni", 0, 10, 5, help="Müşteri kandırıldığını düşünüyor mu?")
        scores['Randevu Sistemi'] = st.slider("İş Kabul Düzeni", 0, 10, 5, help="Randevulu mu çalışılıyor?")
        scores['Google Harita'] = st.slider("Yorum ve Puanlar", 0, 10, 5, help="Sanayide referans çok önemlidir")
        scores['Bilgilendirme'] = st.slider("Süreç Bilgilendirmesi", 0, 10, 5, help="Müşteriye video/fotoğraf atılıyor mu?")
        scores['Kurumsallık'] = st.slider("Bekleme Alanı/Giyim", 0, 10, 5, help="Ustalar temiz giyiniyor mu?")

# 7. EMLAK & DANIŞMANLIK
elif "Emlak" in sektor:
    with col1:
        st.subheader("🏠 Portföy Yönetimi")
        scores['Portföy Genişliği'] = st.slider("İlan Sayısı", 0, 10, 5, help="Elindeki gayrimenkul sayısı yeterli mi?")
        scores['Dönüş Hızı'] = st.slider("Müşteriye Dönüş", 0, 10, 5, help="Arayana ne kadar sürede dönülüyor?")
        scores['Veri Tabanı'] = st.slider("CRM / Müşteri Kaydı", 0, 10, 5, help="Müşteri talepleri kaydediliyor mu?")
        scores['Sözleşme Düzeni'] = st.slider("Resmi Evrak Takibi", 0, 10, 5, help="Yetki belgeleri tam mı?")
        scores['Bölge Hakimiyeti'] = st.slider("Fiyat Analizi", 0, 10, 5, help="Bölgedeki fiyatlara hakim misin?")
    with col2:
        st.subheader("📢 Dijital Pazarlama")
        scores['İlan Kalitesi'] = st.slider("Fotoğraf/Video Çekimi", 0, 10, 5, help="Geniş açı, aydınlık fotoğraflar")
        scores['Sahibinden/Portal'] = st.slider("İlan Açıklamaları", 0, 10, 5, help="Açıklamalar ikna edici mi?")
        scores['Kişisel Marka'] = st.slider("Sosyal Medya Duruşu", 0, 10, 5, help="Emlakçı güven veriyor mu?")
        scores['Video Tur'] = st.slider("Ev Tanıtım Videoları", 0, 10, 5, help="Reels ile ev gezdiriliyor mu?")
        scores['Referanslar'] = st.slider("Mutlu Müşteriler", 0, 10, 5, help="Satış sonrası yorumlar paylaşılıyor mu?")

# 8. E-TİCARET
elif "E-Ticaret" in sektor:
    with col1:
        st.subheader("📦 Lojistik & Depo")
        scores['Kargolama Hızı'] = st.slider("Siparişten Kargoya Süre", 0, 10, 5, help="Aynı gün kargo yapılıyor mu?")
        scores['Stok Takibi'] = st.slider("Entegrasyon Doğruluğu", 0, 10, 5, help="Olmayan ürün satılıyor mu?")
        scores['Paketleme'] = st.slider("Paket Kalitesi", 0, 10, 5, help="Kargo hasar görüyor mu?")
        scores['İade Yönetimi'] = st.slider("İade Oranı", 0, 10, 5, help="İadeler neden kaynaklanıyor?")
        scores['Maliyet Analizi'] = st.slider("Kârlılık Hesabı", 0, 10, 5, help="Komisyon ve kargo sonrası kâr hesabı")
    with col2:
        st.subheader("💻 Dijital Pazarlama")
        scores['Fotoğraf Kalitesi'] = st.slider("Ürün Görselleri", 0, 10, 5, help="Beyaz fon ve mankenli çekimler")
        scores['Reklam (ROAS)'] = st.slider("Reklam Performansı", 0, 10, 5, help="Reklama verilen para dönüyor mu?")
        scores['Sosyal Medya'] = st.slider("Instagram/TikTok", 0, 10, 5, help="Ürün videoları viral oluyor mu?")
        scores['Müşteri Yorumları'] = st.slider("Mağaza Puanı", 0, 10, 5, help="Trendyol/Hepsiburada puanı")
        scores['Kampanya'] = st.slider("Sepet Ortalaması", 0, 10, 5, help="Çoklu alım kampanyaları var mı?")

# --- GRAFİK (RADAR CHART) ---
st.markdown("---")
col_graph, col_result = st.columns([1.5, 1])

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
    if scores:
        ortalama_puan = sum(values) / len(values)
        st.metric(label="GENEL BUERA SKORU", value=f"{ortalama_puan:.1f} / 10")

        if ortalama_puan >= 8:
            st.success("DURUM: MÜKEMMEL 🌟")
            st.write("İşletme çok iyi durumda. Strateji: Koruma ve mikro iyileştirme.")
        elif 6 <= ortalama_puan < 8:
            st.warning("DURUM: İYİ AMA RİSKLİ ⚠️")
            st.write("Kritik süreçlerde iyileştirme yapılırsa ciro %30 artabilir.")
        else:
            st.error("DURUM: KRİTİK 🚨")
            st.write("Acil müdahale gerekli! Ciddi verimlilik ve müşteri kaybı var.")

        st.markdown("---")
        with st.expander("💊 MÜHENDİSLİK REÇETESİ", expanded=True):
            zayif = {k: v for k, v in scores.items() if v < 6}
            if not zayif: st.write("✅ Kritik zayıf nokta yok.")
            else:
                for k, v in zayif.items(): st.markdown(f"- ❌ **{k} ({v}/10):** İyileştirilmeli.")