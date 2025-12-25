import streamlit as st
from streamlit_option_menu import option_menu
import os
import sys

# -----------------------------------------------------
# 1. PAGE CONFIG (MUST BE FIRST)
# -----------------------------------------------------
st.set_page_config(
    page_title="Quantum AQI Forecasting – Neon Cyber Edition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# 2. PATH CONFIGURATION (The "No-Rename" Fix)
# -----------------------------------------------------
# This adds the 'pages' directory to Python's search path
# so you can import 'Home' instead of 'pages.Home'
current_dir = os.path.dirname(os.path.abspath(__file__))
pages_path = os.path.join(current_dir, "pages")
if pages_path not in sys.path:
    sys.path.append(pages_path)

# -----------------------------------------------------
# 3. LOAD CUSTOM CSS
# -----------------------------------------------------
def load_css():
    try:
        with open("dashboard/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        try:
            with open("styles.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except:
            pass # Silent failure for CSS

load_css()

# -----------------------------------------------------
# 4. MAIN TITLE
# -----------------------------------------------------
st.markdown("<h1 class='title-glow'>🌌 Quantum AQI Forecasting – Neon Cyber Edition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Advanced AI + Quantum Dashboard for Air Quality Monitoring</p>", unsafe_allow_html=True)

# -----------------------------------------------------
# 5. SIDEBAR MENU
# -----------------------------------------------------
with st.sidebar:
    selected = option_menu(
        "⚡ Navigation",
        ["Home", "RealTimeAQI", "Forecasting", "QuantumModule", "Heatmap", "AnomalyDetection"],
        icons=["house", "cloud", "graph-up", "cpu", "map", "exclamation-triangle"],
        default_index=0,
        styles={
            "nav-link": {"--hover-color": "#00eaff"},
            "icon": {"color": "#00eaff"},
        }
    )

# -----------------------------------------------------
# 6. PAGE ROUTING
# -----------------------------------------------------
# We import directly by file name because we added 'pages' to the path above
if selected == "Home":
    import Home
    Home.run()

elif selected == "RealTimeAQI":
    import RealTimeAQI
    RealTimeAQI.run()

elif selected == "Forecasting":
    import Forecasting
    Forecasting.run()

elif selected == "QuantumModule":
    import QuantumModule
    QuantumModule.run()

elif selected == "Heatmap":
    import Heatmap
    Heatmap.run()

elif selected == "AnomalyDetection":
    import AnomalyDetection
    AnomalyDetection.run()
