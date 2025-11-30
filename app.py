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

# --- ZORUNLU CSS ---
st.markdown(f"""
<style>
    .stApp {{ background-color: {BRAND_NAVY}; color: {BRAND_WHITE}; }}
    [data-testid="stSidebar"] {{ background-color: {BRAND_INPUT_BG}; }}
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {{ color: {BRAND_WHITE} !important; }}
    [data-testid="stMetricValue"] {{ color: {BRAND_ORANGE} !important; }}
    
    /* GİRİŞ KUTULARI */
    [data-testid="stTextInput"] input {{ background-color: {BRAND_INPUT_BG} !important; color: {BRAND_WHITE} !important; border: 1px solid {BRAND_ORANGE} !important; }}
    
    /* SEÇİM KUTULARI */
    div[data-baseweb="select"] > div {{ background-color: {BRAND_INPUT_BG} !important; color: {BRAND_WHITE} !important; border: 1px solid {BRAND_ORANGE} !important; }}
    div[data-baseweb="popover"] div {{ background-color: {BRAND_INPUT_BG} !important; color: {BRAND_WHITE} !important; }}
    
    /* RAPOR KUTUSU */
    [data-testid="stCodeBlock"] {{ background-color: {BRAND_INPUT_BG} !important; border: 1px solid {BRAND_ORANGE} !important; border-radius: 10px !important; }}
    [data-testid="stCodeBlock"] * {{ background-color: {BRAND_INPUT_BG} !important; color: {BRAND_WHITE} !important; font-family: 'Source Code Pro', monospace !important; }}
    [data-testid="stCodeBlock"] button {{ background-color: transparent !important; color: {BRAND_WHITE} !important; }}
    [data-testid="stCodeBlock"] button:hover {{ color: {BRAND_ORANGE} !important; }}
    
    /* SLIDER VE TOOLTIP */
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{{ background-color: {BRAND_ORANGE}; }}
    .streamlit-expanderHeader {{ color: {BRAND_ORANGE} !important; font-weight: bold; }}
    
    /* Soru İşareti Rengi (Tooltip) */
    [data-testid="stTooltipIcon"] {{ color: {BRAND_ORANGE} !important; }}
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

# --- GENEL REHBER ---
with st.expander("ℹ️ NASIL PUANLAMALIYIM? (Genel Rehber)"):
    st.markdown("""
    **1 - 3 Puan (Kritik):** Süreç yok, her şey manuel, sık hata yapılıyor.
    **4 - 7 Puan (Orta):** Kısmi düzen var ama standartlaşmamış.
    **8 - 10 Puan (Mükemmel):** Sistem tıkır tıkır işliyor, yazılım kullanılıyor.
    """)

scores = {}
col1, col2 = st.columns(2)

# --- SORU HAVUZU (HELP PARAMETRELERİ EKLENDİ) ---

# 1. PERAKENDE
if "Perakende" in sektor:
    with col1:
        st.subheader("🏭 Operasyonel Süreçler")
        scores['Stok Yönetimi'] = st.slider("Stok Doğruluğu", 0, 10, 5, help="1: Ne var bilmiyorum | 10: Barkodlu anlık takip")
        scores['Raf Düzeni'] = st.slider("Ürün Yerleşimi", 0, 10, 5, help="1: Karışık | 10: En çok satanlar göz hizasında, kategorize")
        scores['Depo Düzeni (5S)'] = st.slider("Depo Tertip ve Düzeni", 0, 10, 5, help="1: Aranan bulunamıyor | 10: Her şey etiketli ve yerinde")
        scores['Tedarik Hızı'] = st.slider("Eksik Ürün Tamamlama", 0, 10, 5, help="1: Ürün bitince fark ediliyor | 10: Bitmeden sipariş geçiliyor")
        scores['Hata Önleme'] = st.slider("Etiket/Barkod Hataları", 0, 10, 5, help="1: Fiyatlar yanlış | 10: Etiketler güncel ve doğru")
    with col2:
        st.subheader("🚀 Satış & Dijital")
        scores['Çapraz Satış'] = st.slider("Kasa Önü Ek Satış", 0, 10, 5, help="1: Hiç teklif edilmiyor | 10: Her müşteriye 'yanına şu da lazım mı' deniyor")
        scores['Müşteri Deneyimi'] = st.slider("Mağaza İçi İlgi", 0, 10, 5, help="1: İlgisiz | 10: Güler yüzlü ve çözüm odaklı")
        scores['Google Haritalar'] = st.slider("Google Puanı", 0, 10, 5, help="1: Haritada yokuz | 10: 4.5 üstü puan ve yorumlara cevap veriliyor")
        scores['Instagram Vitrini'] = st.slider("Sosyal Medya Kalitesi", 0, 10, 5, help="1: Paylaşım yok | 10: Profesyonel, düzenli ve Reels odaklı")
        scores['Rakip Analizi'] = st.slider("Fiyat Rekabeti", 0, 10, 5, help="1: Rakipleri bilmiyorum | 10: Fiyatları sürekli takip ediyorum")

# 2. HİZMET
elif "Hizmet" in sektor:
    with col1:
        st.subheader("⏳ Zaman & Kapasite")
        scores['İşlem Hızı'] = st.slider("Standart İşlem Süresi", 0, 10, 5, help="1: Süreler çok değişken | 10: Her işlem standart sürede biter")
        scores['Randevu Sistemi'] = st.slider("Randevu Düzeni", 0, 10, 5, help="1: Defterde karışık | 10: Dijital sistem, SMS hatırlatma var")
        scores['Kapasite'] = st.slider("Koltuk Doluluk Oranı", 0, 10, 5, help="1: Çoğu zaman boş | 10: Randevular full dolu")
        scores['Hazırlık Süresi'] = st.slider("Temizlik Hızı", 0, 10, 5, help="1: Temizlik uzun sürüyor | 10: 2 dakikada koltuk hazır")
        scores['Ergonomi'] = st.slider("Çalışma Alanı", 0, 10, 5, help="1: Malzemeler dağınık | 10: Her şey el altında")
    with col2:
        st.subheader("💎 Marka & Deneyim")
        scores['Sadakat'] = st.slider("Tekrar Gelen Müşteri", 0, 10, 5, help="1: Bir gelen bir daha gelmiyor | 10: Müşterilerim yıllardır sabittir")
        scores['Hizmet Kalitesi'] = st.slider("Müşteri Memnuniyeti", 0, 10, 5, help="1: Şikayet çok | 10: Herkes teşekkür ederek çıkıyor")
        scores['Google Yorumlar'] = st.slider("Harita Puanı", 0, 10, 5, help="1: Kötü yorumlar var | 10: 5 Yıldız ve olumlu yorumlar")
        scores['Video İçerik'] = st.slider("Reels Paylaşımı", 0, 10, 5, help="1: Video çekmiyoruz | 10: Haftalık düzenli işlem videosu atıyoruz")
        scores['Kurumsal İmaj'] = st.slider("Salon Atmosferi", 0, 10, 5, help="1: Mahalle dükkanı | 10: Premium salon havası")

# 3. YEME-İÇME
elif "Yeme-İçme" in sektor:
    with col1:
        st.subheader("🍳 Mutfak & Operasyon")
        scores['Menü Müh.'] = st.slider("Menü Kârlılığı", 0, 10, 5, help="1: Maliyet hesabı yok | 10: Hangi ürün ne kadar kazandırıyor biliyorum")
        scores['Servis Hızı'] = st.slider("Sipariş Süresi", 0, 10, 5, help="1: Müşteri çok bekliyor | 10: Standart sürede masada")
        scores['Mutfak Akışı'] = st.slider("Mutfak Düzeni", 0, 10, 5, help="1: Kaos var | 10: Saat gibi işleyen sistem")
        scores['Atık Yönetimi'] = st.slider("Gıda İsrafı", 0, 10, 5, help="1: Çok yemek çöpe gidiyor | 10: Atık sıfıra yakın")
        scores['Hijyen (5S)'] = st.slider("Temizlik", 0, 10, 5, help="1: Gözle görülür kirlilik | 10: Bal dök yala")
    with col2:
        st.subheader("📈 Satış & Yönetim")
        scores['Masa Devri'] = st.slider("Sirkülasyon", 0, 10, 5, help="1: Müşteri 1 çayla 3 saat oturuyor | 10: Masalar sürekli dolup boşalıyor")
        scores['Stok (FIFO)'] = st.slider("Depo Yönetimi", 0, 10, 5, help="1: SKT geçen ürün çıkıyor | 10: İlk giren ilk çıkar kuralı var")
        scores['Standart Reçete'] = st.slider("Lezzet Standardı", 0, 10, 5, help="1: Usta değişince tat değişiyor | 10: Gramajlar ve tarif sabit")
        scores['Dijital Menü'] = st.slider("QR ve Online", 0, 10, 5, help="1: Sadece kağıt menü | 10: QR menü ve online sipariş aktif")
        scores['Puan Durumu'] = st.slider("Platform Puanları", 0, 10, 5, help="1: Şikayet çok | 10: Şehrin en iyisi yorumları")

# 4. MARKET
elif "Market" in sektor:
    with col1:
        st.subheader("🛒 Market Operasyonları")
        scores['Raf Bulunurluğu'] = st.slider("Raf Doluluk Oranı", 0, 10, 5, help="1: Raflar sık sık boş kalıyor | 10: Raflar her zaman dolu")
        scores['SKT Yönetimi'] = st.slider("Son Kullanma Takibi", 0, 10, 5, help="1: Tarihi geçen ürünler rafta | 10: Günlük kontrol yapılıyor")
        scores['Kasa Kuyruğu'] = st.slider("Kasa İşlem Hızı", 0, 10, 5, help="1: Kuyruklar çok uzun | 10: Kasa akışı çok hızlı")
        scores['Depo Düzeni'] = st.slider("Depo ve İstifleme", 0, 10, 5, help="1: Depo karışık | 10: Ürünler kategorize edilmiş")
        scores['Temizlik'] = st.slider("Mağaza Temizliği", 0, 10, 5, help="1: Yerler/raflar kirli | 10: Sürekli temizleniyor")
    with col2:
        st.subheader("📣 Pazarlama & Yerel")
        scores['İndirim/Insert'] = st.slider("Kampanya Yönetimi", 0, 10, 5, help="1: Kampanya yok | 10: Haftalık indirim broşürü var")
        scores['Müşteri Sadakati'] = st.slider("Sadakat Kartı/Veresiye", 0, 10, 5, help="1: Müşteri takibi yok | 10: Sadakat kartı sistemi var")
        scores['Google Harita'] = st.slider("Yerel Görünürlük", 0, 10, 5, help="1: Haritada yanlış konum | 10: Fotoğraflı ve yorumlu profil")
        scores['Sosyal Medya'] = st.slider("Ürün Paylaşımları", 0, 10, 5, help="1: Hiç yok | 10: Yeni ürünler paylaşılıyor")
        scores['Sepet Büyüklüğü'] = st.slider("Ortalama Sepet", 0, 10, 5, help="1: Sadece ekmek alıp çıkıyorlar | 10: Sepet dolu çıkıyorlar")

# 5. SPOR SALONU
elif "Spor Salonu" in sektor:
    with col1:
        st.subheader("💪 Salon Verimliliği")
        scores['Ekipman Bakımı'] = st.slider("Aletlerin Durumu", 0, 10, 5, help="1: Çoğu alet bozuk/eski | 10: Hepsi yeni ve bakımlı")
        scores['Kapasite (Pik)'] = st.slider("Yoğun Saat Yönetimi", 0, 10, 5, help="1: Akşamları alet sırası bekleniyor | 10: Akış rahat")
        scores['Hijyen'] = st.slider("Temizlik ve Koku", 0, 10, 5, help="1: Ter kokusu ve kir var | 10: Salon mis gibi kokuyor")
        scores['Enerji'] = st.slider("Gider Yönetimi", 0, 10, 5, help="1: Işıklar gereksiz yanıyor | 10: Tasarruflu sistemler var")
        scores['Personel'] = st.slider("Antrenör İlgisi", 0, 10, 5, help="1: Hocalar telefona bakıyor | 10: Üyelerle birebir ilgileniyorlar")
    with col2:
        st.subheader("🔥 Üye & Pazarlama")
        scores['Üye Devamlılığı'] = st.slider("Retention (Yenileme)", 0, 10, 5, help="1: Kayıt olan bir ay sonra bırakıyor | 10: Üyeler yıllardır burada")
        scores['Dönüşüm'] = st.slider("Before/After Paylaşımı", 0, 10, 5, help="1: Hiç yok | 10: Üye değişim hikayeleri paylaşılıyor")
        scores['Google Yorumlar'] = st.slider("Salon Puanı", 0, 10, 5, help="1: Kötü yorumlar | 10: Şehrin en iyisi")
        scores['Instagram'] = st.slider("Motivasyon İçerikleri", 0, 10, 5, help="1: Hesap boş | 10: Antrenman videoları atılıyor")
        scores['Kampanya'] = st.slider("Yeni Üye Kazanımı", 0, 10, 5, help="1: Bekliyoruz | 10: Dönemsel kampanyalar yapılıyor")

# 6. OTO SERVİS
elif "Oto Servis" in sektor:
    with col1:
        st.subheader("🔧 Servis Operasyonu")
        scores['Arıza Tespit'] = st.slider("Teşhis Doğruluğu", 0, 10, 5, help="1: Deneme yanılma yapılıyor | 10: Nokta atışı tespit")
        scores['Parça Tedariği'] = st.slider("Yedek Parça Lojistiği", 0, 10, 5, help="1: Parça günlerce bekleniyor | 10: Parça hemen geliyor")
        scores['Lift Kullanımı'] = st.slider("Alan Verimliliği", 0, 10, 5, help="1: Lifler boş kalıyor | 10: Sürekli araç giriş çıkışı var")
        scores['Takım Düzeni'] = st.slider("5S (Takımhane)", 0, 10, 5, help="1: Anahtarlar kayıp | 10: Her şey panoda asılı")
        scores['Teslimat Süresi'] = st.slider("Söz Verilen Süre", 0, 10, 5, help="1: Sürekli gecikiyor | 10: Tam zamanında teslim")
    with col2:
        st.subheader("🤝 Müşteri & Güven")
        scores['Güvenilirlik'] = st.slider("Müşteri Güveni", 0, 10, 5, help="1: Müşteri şüpheci | 10: Anahtarını bırakıp gidiyor")
        scores['Randevu'] = st.slider("İş Kabul Düzeni", 0, 10, 5, help="1: Rastgele | 10: Randevulu sistem")
        scores['Google Harita'] = st.slider("Yorum ve Puanlar", 0, 10, 5, help="1: Şikayet çok | 10: Tavsiye ediliyor")
        scores['Bilgilendirme'] = st.slider("Süreç Bilgilendirmesi", 0, 10, 5, help="1: Müşteri arayıp soruyor | 10: Müşteriye video/foto atılıyor")
        scores['Kurumsallık'] = st.slider("Giyim ve Bekleme", 0, 10, 5, help="1: Kirli tulumlar | 10: Temiz üniforma ve bekleme salonu")

# 7. EMLAK
elif "Emlak" in sektor:
    with col1:
        st.subheader("🏠 Portföy Yönetimi")
        scores['Portföy'] = st.slider("İlan Sayısı", 0, 10, 5, help="1: Elde az ev var | 10: Portföy çok geniş")
        scores['Dönüş Hızı'] = st.slider("Müşteriye Dönüş", 0, 10, 5, help="1: Telefonlara dönülmüyor | 10: Anında geri dönüş")
        scores['Veri Tabanı'] = st.slider("CRM / Müşteri Kaydı", 0, 10, 5, help="1: Defterde yazılı | 10: Dijital müşteri takibi")
        scores['Evrak'] = st.slider("Sözleşme Düzeni", 0, 10, 5, help="1: Eksik evrak | 10: Her şey hukuka uygun")
        scores['Bölge Hakimiyeti'] = st.slider("Fiyat Analizi", 0, 10, 5, help="1: Fiyatlar tahmini | 10: Bölge rayici biliniyor")
    with col2:
        st.subheader("📢 Dijital Pazarlama")
        scores['İlan Kalitesi'] = st.slider("Fotoğraf Çekimi", 0, 10, 5, help="1: Karanlık, kötü açılı | 10: Profesyonel geniş açı, aydınlık")
        scores['Açıklama'] = st.slider("İlan Metinleri", 0, 10, 5, help="1: Detaysız | 10: Hikayeleştirilmiş, ikna edici")
        scores['Kişisel Marka'] = st.slider("Sosyal Medya Duruşu", 0, 10, 5, help="1: Güven vermiyor | 10: Emlak Uzmanı profili")
        scores['Video Tur'] = st.slider("Ev Tanıtım Videoları", 0, 10, 5, help="1: Yok | 10: Reels ile ev gezdiriliyor")
        scores['Referanslar'] = st.slider("Mutlu Müşteriler", 0, 10, 5, help="1: Yok | 10: Tapu töreni fotoları paylaşılıyor")

# 8. E-TİCARET
elif "E-Ticaret" in sektor:
    with col1:
        st.subheader("📦 Lojistik & Depo")
        scores['Kargolama'] = st.slider("Kargo Hızı", 0, 10, 5, help="1: 3 günde kargo | 10: Aynı gün kargo")
        scores['Stok Takibi'] = st.slider("Entegrasyon", 0, 10, 5, help="1: Olmayan ürün satılıyor | 10: Tam entegre stok")
        scores['Paketleme'] = st.slider("Paket Kalitesi", 0, 10, 5, help="1: Özensiz, hasarlı | 10: Markalı kutu, hediye paketi")
        scores['İade'] = st.slider("İade Oranı", 0, 10, 5, help="1: Çok iade var | 10: İade çok az")
        scores['Maliyet'] = st.slider("Kârlılık Hesabı", 0, 10, 5, help="1: Kâr belirsiz | 10: Komisyon sonrası net kâr biliniyor")
    with col2:
        st.subheader("💻 Dijital Pazarlama")
        scores['Fotoğraf'] = st.slider("Ürün Görselleri", 0, 10, 5, help="1: Amatör çekim | 10: Stüdyo çekimi, mankenli")
        scores['Reklam'] = st.slider("Reklam Performansı", 0, 10, 5, help="1: Boşa para harcanıyor | 10: ROAS yüksek")
        scores['Sosyal Medya'] = st.slider("Instagram/TikTok", 0, 10, 5, help="1: Pasif | 10: Viral videolar, aktif story")
        scores['Puan'] = st.slider("Mağaza Puanı", 0, 10, 5, help="1: Düşük puan | 10: 9.5 üzeri puan")
        scores['Kampanya'] = st.slider("Sepet Ortalaması", 0, 10, 5, help="1: Tek ürün alınıyor | 10: Çoklu alım stratejisi var")

# --- GRAFİK ---
st.markdown("---")
col_graph, col_result = st.columns([1.5, 1])

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

with col_result:
    st.subheader("🏆 Analiz Sonucu")
    st.metric(label="GENEL BUERA SKORU", value=f"{ortalama_puan:.1f} / 10")

    if ortalama_puan >= 8:
        st.success("DURUM: MÜKEMMEL 🌟")
    elif 6 <= ortalama_puan < 8:
        st.warning("DURUM: İYİ AMA RİSKLİ ⚠️")
    else:
        st.error("DURUM: KRİTİK 🚨")

    st.markdown("---")
    with st.expander("💊 MÜHENDİSLİK REÇETESİ", expanded=True):
        if not zayif_noktalar: st.write("✅ Kritik zayıf nokta yok.")
        else:
            for k, v in zayif_noktalar.items(): st.markdown(f"- ❌ **{k} ({v}/10):** İyileştirilmeli.")

# --- RAPOR ---
st.markdown("---")
st.subheader("🚀 SONUÇLARI BİZE İLETİN")
st.info("Bu analizi uzman ekibimizle paylaşarak işletmenize özel ücretsiz yol haritasını alın.")

rapor_metni = f"""
Merhaba BUERA,
İşletme Analiz Sonuçlarım:

📋 İşletme: {isletme_adi} ({yetkili})
🏭 Sektör: {sektor}
🏆 BUERA Skorum: {ortalama_puan:.1f} / 10

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