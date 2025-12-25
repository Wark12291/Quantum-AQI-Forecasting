import streamlit as st
from streamlit_option_menu import option_menu

# -----------------------------------------------------
# PAGE CONFIG MUST COME FIRST
# -----------------------------------------------------
st.set_page_config(
    page_title="Quantum AQI Forecasting – Neon Cyber Edition",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# LOAD CUSTOM CSS (AFTER page_config)
# -----------------------------------------------------
def load_css():
    try:
        with open("dashboard/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        st.error("❌ Could not load styles.css")

load_css()

# -----------------------------------------------------
# MAIN TITLE
# -----------------------------------------------------
st.markdown("<h1 class='title-glow'>🌌 Quantum AQI Forecasting – Neon Cyber Edition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Advanced AI + Quantum Dashboard for Air Quality Monitoring</p>", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR MENU
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
# PAGE ROUTING
# -----------------------------------------------------
if selected == "Home":
    from pages import Home as page
    page.run()

elif selected == "RealTimeAQI":
    from pages import RealTimeAQI as page
    page.run()

elif selected == "Forecasting":
    from pages import Forecasting as page
    page.run()

elif selected == "QuantumModule":
    from pages import QuantumModule as page
    page.run()

elif selected == "Heatmap":
    from pages import Heatmap as page
    page.run()

elif selected == "AnomalyDetection":
    from pages import AnomalyDetection as page
    page.run()
