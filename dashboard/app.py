import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Quantum AQI Forecasting – Neon Cyber Edition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
def load_css():
    try:
        with open("dashboard/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        st.error("❌ Could not load styles.css")

load_css()

# -------------------------------
# CORRECT IMPORTS (VERY IMPORTANT)
# -------------------------------
from pages import Home
from pages import RealTimeAQI
from pages import Forecasting
from pages import QuantumModule
from pages import Heatmap
from pages import AnomalyDetection

# Header
st.markdown("<h1 class='title-glow'>🌌 Quantum AQI Forecasting – Neon Cyber Edition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI + Quantum Hybrid Dashboard</p>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "⚡ Menu",
        ["Home", "RealTimeAQI", "Forecasting", "QuantumModule", "Heatmap", "AnomalyDetection"],
        icons=["house", "cloud", "graph-up", "cpu", "map", "exclamation-triangle"],
        default_index=0,
    )

# Routing
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
