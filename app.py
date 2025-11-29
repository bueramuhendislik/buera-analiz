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
    /* Expander (Rehber) kutusunun rengini ayarla */
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
    st.warning("⚠️ Logo yüklenemedi.")
    st.title("BUERA")

st.markdown(f"<h3 style='color:{BRAND_ORANGE};'>Veri Odaklı İşletme Analiz Kokpiti</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ ---
st.sidebar.header("📋 İşletme Kimliği")
isletme_adi = st.sidebar.text_input("İşletme Adı", "Örnek İşletme")
sektor = st.sidebar.selectbox("Sektör Seçimi", ["Perakende (Telefon/Kırtasiye)", "Hizmet (Berber/Güzellik)", "Yeme-İçme (Kafe/Restoran)"])

st.sidebar.markdown("---")
st.sidebar.info("Bu analiz, BUERA Endüstri Mühendisliği algoritmalarıyla hesaplanmaktadır.")
st.sidebar.caption("© 2024 BUERA Engineering")

# --- ANALİZ MOTORU ---
st.header(f"📊 {isletme_adi} | {sektor} Analizi")

# --- PUANLAMA REHBERİ FONKSİYONU ---
def puanlama_rehberi_goster():
    with st.expander("ℹ️ NASIL PUANLAMALIYIM? (Rehberi Gör)"):
        st.markdown("""
        **1 - 3 Puan (Kritik):** Süreç yok, her şey kafada/manuel, hatalar sık oluyor.
        **4 - 7 Puan (Orta):** Bazı kurallar var ama her zaman uygulanmıyor, kısmi düzen var.
        **8 - 10 Puan (Mükemmel):** Yazılımlar/Sistemler kullanılıyor, hata sıfıra yakın, tam otomatik.
        """)

puanlama_rehberi_goster()

scores = {}
col1, col2 = st.columns(2)

# Sektöre Göre Sorular ve İPUÇLARI (Help Parametresi Eklendi)
if sektor == "Perakende (Telefon/Kırtasiye)":
    with col1:
        st.subheader("🏭 Operasyonel Süreçler")
        scores['Stok Yönetimi'] = st.slider("Stok Doğruluğu", 0, 10, 5, help="1: Ne var bilmiyorum / 10: Barkodlu anlık takip")
        scores['Raf Düzeni'] = st.slider("Ürün Yerleşimi", 0, 10, 5, help="1: Karışık / 10: En çok satanlar göz hizasında, kategorize")
        scores['Depo Düzeni (5S)'] = st.slider("Depo Tertip ve Düzeni", 0, 10, 5, help="1: Aranan bulunamıyor / 10: Her şey etiketli ve yerinde")
        scores['Tedarik Hızı'] = st.slider("Eksik Ürün Tamamlama", 0, 10, 5, help="1: Ürünler bitince fark ediliyor / 10: Bitmeden sipariş geçiliyor")
        scores['Hata Önleme'] = st.slider("Barkod/Etiket Hataları", 0, 10, 5, help="1: Fiyatlar yanlış / 10: Etiketler güncel ve doğru")
    with col2:
        st.subheader("🚀 Satış & Dijital")
        scores['Çapraz Satış'] = st.slider("Kasa Önü Ek Satış", 0, 10, 5, help="1: Hiç teklif edilmiyor / 10: Her müşteriye 'yanına şu da lazım mı' deniyor")
        scores['Müşteri Deneyimi'] = st.slider("Mağaza İçi İlgi", 0, 10, 5, help="1: İlgisiz / 10: Güler yüzlü ve çözüm odaklı karşılama")
        scores['Google Haritalar'] = st.slider("Google Puanı ve Yorumlar", 0, 10, 5, help="1: Haritada yokuz / 10: 4.5 üstü puan ve yorumlara cevap veriliyor")
        scores['Instagram Vitrini'] = st.slider("Sosyal Medya Kalitesi", 0, 10, 5, help="1: Paylaşım yok / 10: Profesyonel, düzenli ve Reels odaklı")
        scores['Rakip Analizi'] = st.slider("Rekabet Durumu", 0, 10, 5, help="1: Rakipleri bilmiyorum / 10: Rakiplerin fiyatlarını ve stratejilerini takip ediyorum")

elif sektor == "Hizmet (Berber/Güzellik)":
    with col1:
        st.subheader("⏳ Zaman & Kapasite")
        scores['İşlem Hızı'] = st.slider("Standart İşlem Süresi", 0, 10, 5, help="1: Bazen 20dk bazen 1 saat sürüyor / 10: Her işlem standart sürede biter")
        scores['Randevu Sistemi'] = st.slider("Randevu Düzeni", 0, 10, 5, help="1: Defterde karışık / 10: Dijital sistem, SMS hatırlatma var")
        scores['Kapasite'] = st.slider("Koltuk Doluluk Oranı", 0, 10, 5, help="1: Çoğu zaman boş / 10: Randevular full dolu")
        scores['Hazırlık Süresi'] = st.slider("Temizlik Hızı", 0, 10, 5, help="1: Müşteri kalkınca temizlik uzun sürüyor / 10: 2 dakikada koltuk hazır")
        scores['Ergonomi'] = st.slider("Çalışma Alanı", 0, 10, 5, help="1: Malzemeler dağınık / 10: Her şey el altında")
    with col2:
        st.subheader("💎 Müşteri & Marka")
        scores['Sadakat'] = st.slider("Tekrar Gelen Müşteri", 0, 10, 5, help="1: Bir gelen bir daha gelmiyor / 10: Müşterilerim yıllardır sabittir")
        scores['Hizmet Kalitesi'] = st.slider("Müşteri Memnuniyeti", 0, 10, 5, help="1: Şikayet çok / 10: Herkes teşekkür ederek çıkıyor")
        scores['Google Yorumlar'] = st.slider("Harita Puanı", 0, 10, 5, help="1: Kötü yorumlar var / 10: 5 Yıldız ve olumlu yorumlar")
        scores['Video İçerik'] = st.slider("Reels Paylaşımı", 0, 10, 5, help="1: Video çekmiyoruz / 10: Haftalık düzenli tıraş/işlem videosu atıyoruz")
        scores['Marka İmajı'] = st.slider("Kurumsal Duruş", 0, 10, 5, help="1: Mahalle berberi / 10: Premium salon havası")

elif sektor == "Yeme-İçme (Kafe/Restoran)":
    with col1:
        st.subheader("🍳 Mutfak & Operasyon")
        scores['Menü Müh.'] = st.slider("Menü Kârlılığı", 0, 10, 5, help="1: Maliyet hesabı yok / 10: Hangi ürün ne kadar kazandırıyor biliyorum")
        scores['Servis Hızı'] = st.slider("Sipariş Süresi", 0, 10, 5, help="1: Müşteri çok bekliyor / 10: Standart sürede masada")
        scores['Mutfak Akışı'] = st.slider("Mutfak Düzeni", 0, 10, 5, help="1: Kaos ve çarpışma var / 10: Saat gibi işleyen sistem")
        scores['Atık Yönetimi'] = st.slider("Gıda İsrafı", 0, 10, 5, help="1: Çok yemek çöpe gidiyor / 10: Atık sıfıra yakın")
        scores['Hijyen (5S)'] = st.slider("Temizlik", 0, 10, 5, help="1: Gözle görülür kirlilik / 10: Bal dök yala")
    with col2:
        st.subheader("📈 Satış & Yönetim")
        scores['Masa Devri'] = st.slider("Sirkülasyon", 0, 10, 5, help="1: Müşteri 1 çayla 3 saat oturuyor / 10: Masalar sürekli dolup boşalıyor")
        scores['Stok (FIFO)'] = st.slider("Depo Yönetimi", 0, 10, 5, help="1: SKT geçen ürün çıkıyor / 10: İlk giren ilk çıkar kuralı var")
        scores['Standart Reçete'] = st.slider("Lezzet Standardı", 0, 10, 5, help="1: Usta değişince tat değişiyor / 10: Gramajlar ve tarif sabit")
        scores['Dijital Menü'] = st.slider("QR ve Online", 0, 10, 5, help="1: Sadece kağıt menü / 10: QR menü ve online sipariş aktif")
        scores['Müşteri Yorumları'] = st.slider("Puan Durumu", 0, 10, 5, help="1: Lezzet/Servis şikayeti çok / 10: Şehrin en iyisi deniyor")

# --- GRAFİK ---
st.markdown("---")
col_graph, col_result = st.columns([1.5, 1])

with col_graph:
    st.subheader("🕸️ Performans Radarı")
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