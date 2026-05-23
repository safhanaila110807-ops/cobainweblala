import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

# ======================================
# CONFIG HALAMAN
# ======================================

st.set_page_config(
    page_title="Kalkulator Gas Ideal",
    page_icon="🧪",
    layout="wide"
)

# ======================================
# JUDUL
# ======================================

st.title("🧪 Kalkulator Gas Ideal Interaktif")
st.markdown("### Hukum Gas + Animasi + Grafik")

# ======================================
# SIDEBAR
# ======================================

menu = st.sidebar.radio(
    "📌 Pilih Menu",
    [
        "🏠 Home",
        "📘 Kalkulator Gas",
        "🎬 Studi Kasus Animasi",
        "📈 Grafik Hubungan"
    ]
)

# ======================================
# HOME
# ======================================

if menu == "🏠 Home":

    st.header("Selamat Datang 👋")

    st.write("""
    Aplikasi ini memiliki fitur:
    
    ✅ Kalkulator hukum gas  
    ✅ Animasi studi kasus  
    ✅ Grafik hubungan variabel gas  
    
    Dibuat menggunakan Python dan Streamlit.
    """)

# ======================================
# KALKULATOR GAS
# ======================================

elif menu == "📘 Kalkulator Gas":

    st.header("📘 Kalkulator Hukum Gas")

    pilihan = st.selectbox(
        "Pilih Hukum Gas",
        [
            "Hukum Boyle",
            "Hukum Charles",
            "Hukum Gay-Lussac",
            "Hukum Avogadro",
            "Persamaan Gas Ideal"
        ]
    )

    # ======================================
    # HUKUM BOYLE
    # ======================================

    if pilihan == "Hukum Boyle":

        st.subheader("Hukum Boyle")
        st.latex(r"P_1V_1 = P_2V_2")

        P1 = st.number_input("P1", value=1.0)
        V1 = st.number_input("V1", value=1.0)
        P2 = st.number_input("P2", value=1.0)

        if st.button("Hitung V2"):

            if P2 != 0:
                V2 = (P1 * V1) / P2
                st.success(f"V2 = {V2:.3f}")
            else:
                st.error("P2 tidak boleh nol")

    # ======================================
    # HUKUM CHARLES
    # ======================================

    elif pilihan == "Hukum Charles":

        st.subheader("Hukum Charles")
        st.latex(r"\frac{V_1}{T_1} = \frac{V_2}{T_2}")

        V1 = st.number_input("V1", value=1.0)
        T1 = st.number_input("T1 (K)", value=273.0)
        T2 = st.number_input("T2 (K)", value=300.0)

        if st.button("Hitung V2"):

            if T1 != 0:
                V2 = (V1 * T2) / T1
                st.success(f"V2 = {V2:.3f}")
            else:
                st.error("T1 tidak boleh nol")

    # ======================================
    # HUKUM GAY-LUSSAC
    # ======================================

    elif pilihan == "Hukum Gay-Lussac":

        st.subheader("Hukum Gay-Lussac")
        st.latex(r"\frac{P_1}{T_1} = \frac{P_2}{T_2}")

        P1 = st.number_input("P1", value=1.0)
        T1 = st.number_input("T1 (K)", value=273.0)
        T2 = st.number_input("T2 (K)", value=300.0)

        if st.button("Hitung P2"):

            if T1 != 0:
                P2 = (P1 * T2) / T1
                st.success(f"P2 = {P2:.3f}")
            else:
                st.error("T1 tidak boleh nol")

    # ======================================
    # HUKUM AVOGADRO
    # ======================================

    elif pilihan == "Hukum Avogadro":

        st.subheader("Hukum Avogadro")
        st.latex(r"\frac{V_1}{n_1} = \frac{V_2}{n_2}")

        V1 = st.number_input("V1", value=1.0)
        n1 = st.number_input("n1", value=1.0)
        n2 = st.number_input("n2", value=2.0)

        if st.button("Hitung V2"):

            if n1 != 0:
                V2 = (V1 * n2) / n1
                st.success(f"V2 = {V2:.3f}")
            else:
                st.error("n1 tidak boleh nol")

    # ======================================
    # GAS IDEAL
    # ======================================

    elif pilihan == "Persamaan Gas Ideal":

        st.subheader("Persamaan Gas Ideal")
        st.latex(r"PV = nRT")

        P = st.number_input("Tekanan (atm)", value=1.0)
        V = st.number_input("Volume (L)", value=1.0)
        n = st.number_input("Mol (n)", value=1.0)

        R = 0.0821

        if st.button("Hitung Suhu"):

            if n != 0:
                T = (P * V) / (n * R)
                st.success(f"Suhu = {T:.2f} K")
            else:
                st.error("Jumlah mol tidak boleh nol")

# ======================================
# ANIMASI STUDI KASUS
# ======================================

elif menu == "🎬 Studi Kasus Animasi":

    st.header("🎬 Studi Kasus Gas Ideal")

    st.write("""
    Diketahui:
    
    - Tekanan = 1 atm
    - Volume = 5 L
    - Mol = 1 mol
    
    Tentukan suhu gas.
    """)

    st.latex(r"PV = nRT")

    P = 1
    V = 5
    n = 1
    R = 0.0821

    if st.button("Mulai Simulasi"):

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        T = (P * V) / (n * R)

        st.success(f"Hasil suhu gas = {T:.2f} K")

        # ======================================
        # ANIMASI PARTIKEL
        # ======================================

        x = np.random.uniform(0.42, 0.58, 50)
        y = np.random.uniform(0.0, 1.0, 50)

        fig = go.Figure()

        fig.add_shape(
            type="rect",
            x0=0.4,
            y0=0,
            x1=0.6,
            y1=1,
            line=dict(width=3)
        )

        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode='markers',
                marker=dict(size=10)
            )
        )

        fig.update_layout(
            title="Simulasi Partikel Gas",
            width=500,
            height=600,
            showlegend=False
        )

        st.plotly_chart(fig)

# ======================================
# GRAFIK
# ======================================

elif menu == "📈 Grafik Hubungan":

    st.header("📈 Grafik Hubungan Variabel")

    grafik = st.selectbox(
        "Pilih Grafik",
        [
            "Tekanan vs Volume",
            "Volume vs Suhu",
            "Tekanan vs Suhu"
        ]
    )

    # ======================================
    # TEKANAN VS VOLUME
    # ======================================

    if grafik == "Tekanan vs Volume":

        V = np.linspace(1, 10, 100)
        P = 10 / V

        fig, ax = plt.subplots()

        ax.plot(V, P)

        ax.set_xlabel("Volume")
        ax.set_ylabel("Tekanan")
        ax.set_title("Grafik Boyle")

        st.pyplot(fig)

    # ======================================
    # VOLUME VS SUHU
    # ======================================

    elif grafik == "Volume vs Suhu":

        T = np.linspace(200, 500, 100)
        V = T / 100

        fig, ax = plt.subplots()

        ax.plot(T, V)

        ax.set_xlabel("Suhu (K)")
        ax.set_ylabel("Volume")
        ax.set_title("Grafik Charles")

        st.pyplot(fig)

    # ======================================
    # TEKANAN VS SUHU
    # ======================================

    elif grafik == "Tekanan vs Suhu":

        T = np.linspace(200, 500, 100)
        P = T / 100

        fig, ax = plt.subplots()

        ax.plot(T, P)

        ax.set_xlabel("Suhu (K)")
        ax.set_ylabel("Tekanan")
        ax.set_title("Grafik Gay-Lussac")

        st.pyplot(fig)

# ======================================
# FOOTER
# ======================================

st.markdown("---")
st.caption("Dibuat dengan Streamlit 🚀")
