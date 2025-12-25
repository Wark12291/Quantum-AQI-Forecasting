import streamlit as st
from streamlit_option_menu import option_menu

# Load custom styles
with open("dashboard/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Quantum AQI Forecasting – Neon Cyber Edition",
    layout="wide"
)

st.markdown("<h1 class='title-glow'>🌌 Quantum AQI Forecasting – Neon Cyber Edition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Advanced AI + Quantum Dashboard for Tirupati Air Quality Monitoring</p>", unsafe_allow_html=True)

st.sidebar.markdown("<h2 class='sidebar-title'>⚡ Navigation</h2>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "RealTimeAQI", "Forecasting", "QuantumModule", "Heatmap", "AnomalyDetection"],
        icons=["house", "cloud", "graph-up", "cpu", "map", "exclamation-triangle"],
        menu_icon="cast",
        default_index=0,
    )

# Page Routing
if selected == "Home":
    import dashboard.pages.Home as page
    page.run()

elif selected == "RealTimeAQI":
    import dashboard.pages.RealTimeAQI as page
    page.run()

elif selected == "Forecasting":
    import dashboard.pages.Forecasting as page
    page.run()

elif selected == "QuantumModule":
    import dashboard.pages.QuantumModule as page
    page.run()

elif selected == "Heatmap":
    import dashboard.pages.Heatmap as page
    page.run()

elif selected == "AnomalyDetection":
    import dashboard.pages.AnomalyDetection as page
    page.run()
