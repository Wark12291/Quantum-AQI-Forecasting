import streamlit as st
from streamlit_option_menu import option_menu

# -----------------------------------------------------
# PAGE CONFIG FIRST
# -----------------------------------------------------
st.set_page_config(
    page_title="Quantum AQI Forecasting – Neon Cyber Edition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# LOAD CSS
# -----------------------------------------------------
def load_css():
    try:
        with open("dashboard/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        st.error("❌ Could not load styles.css")

load_css()

# -----------------------------------------------------
# IMPORT PAGES (CORRECT FORMAT)
# -----------------------------------------------------
import pages.Home as Home
import pages.RealTimeAQI as RealTimeAQI
import pages.Forecasting as Forecasting
import pages.QuantumModule as QuantumModule
import pages.Heatmap as Heatmap
import pages.AnomalyDetection as AnomalyDetection

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------
st.markdown("<h1 class='title-glow'>🌌 Quantum AQI Forecasting – Neon Cyber Edition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI + Quantum Hybrid Dashboard</p>", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR MENU
# -----------------------------------------------------
with st.sidebar:
    selected = option_menu(
        "⚡ Menu",
        ["Home", "RealTimeAQI", "Forecasting", "QuantumModule", "Heatmap", "AnomalyDetection"],
        icons=["house", "cloud", "graph-up", "cpu", "map", "exclamation-triangle"],
        default_index=0,
    )

# -----------------------------------------------------
# ROUTING
# -----------------------------------------------------
if selected == "Home":
    Home.run()

elif selected == "RealTimeAQI":
    RealTimeAQI.run()

elif selected == "Forecasting":
    Forecasting.run()

elif selected == "QuantumModule":
    QuantumModule.run()

elif selected == "Heatmap":
    Heatmap.run()

elif selected == "AnomalyDetection":
    AnomalyDetection.run()
