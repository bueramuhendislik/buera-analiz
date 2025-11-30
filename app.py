import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- MARKA RENKLERİ ---
BRAND_NAVY = '#0F172A'
BRAND_ORANGE = '#F59E0B'
BRAND_WHITE = '#F8FAFC'
BRAND_INPUT_BG = '#1E293B'

# Sayfayı GENİŞ moda alıyoruz ki yan yana sığsınlar
st.set_page_config(page_title="BUERA Video Modu", layout="wide")

# --- CSS (GÖRÜNTÜYÜ TEMİZLEME) ---
st.markdown(f"""
<style>
    /* Arka planı ve yazıları ayarla */
    .stApp {{ background-color: {BRAND_NAVY}; color: {BRAND_WHITE}; }}
    h1, h2, h3, p, span, div, label {{ color: {BRAND_WHITE} !important; }}
    
    /* Üstteki boşluğu yok et (Kamera açısı için) */
    .block-container {{ padding-top: 1rem; padding-bottom: 0rem; }}
    
    /* Slider Renkleri */
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{{
        background-color: {BRAND_ORANGE};
    }}
    
    /* Metrik Değerleri */
    [data-testid="stMetricValue"] {{ color: {BRAND_ORANGE} !important; }}
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
st.markdown(f"<h2 style='text-align: center; color: {BRAND_ORANGE};'>BUERA ANALİZ SİSTEMİ</h2>", unsafe_allow_html=True)

# --- EKRANI İKİYE BÖLÜYORUZ (SOL: AYARLAR / SAĞ: GRAFİK) ---
col_left, col_right = st.columns([1, 1.5]) # Sağ taraf biraz daha geniş olsun

with col_left:
    st.info("👇 VERİLERİ GİRİN")
    # Hızlı hareket ettirebileceğin basit sliderlar
    s1 = st.slider("Stok Yönetimi", 0, 10, 4)
    s2 = st.slider("Hizmet Hızı", 0, 10, 6)
    s3 = st.slider("Dijital Vitrin", 0, 10, 3)
    s4 = st.slider("Müşteri Memnuniyeti", 0, 10, 7)
    s5 = st.slider("Rakip Analizi", 0, 10, 5)
    
    st.write("")
    st.markdown("### 🎯 SKOR: 8.2") 

with col_right:
    # GRAFİK VERİLERİ
    categories = ['Stok', 'Hız', 'Dijital', 'Müşteri', 'Rakip']
    values = [s1, s2, s3, s4, s5]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values, 
        theta=categories, 
        fill='toself', 
        name='Analiz',
        line_color=BRAND_ORANGE, 
        fillcolor='rgba(245, 158, 11, 0.5)', # Turuncu Dolgu
        marker=dict(color=BRAND_ORANGE)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(color=BRAND_WHITE), gridcolor='#334155'),
            angularaxis=dict(tickfont=dict(color=BRAND_WHITE, size=15), gridcolor='#334155'), # Yazılar BÜYÜK
            bgcolor=BRAND_NAVY
        ),
        paper_bgcolor=BRAND_NAVY, 
        showlegend=False,
        height=550, # Grafik kocaman olsun
        margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)