import streamlit as st
import datetime

def run():

    # Title
    st.markdown("<h2 class='title-glow'>🚀 Welcome to the Quantum AQI Forecasting Dashboard</h2>", unsafe_allow_html=True)

    # Subtitle
    st.markdown(
        "<p class='subtitle'>AI + Quantum Powered Air Quality Monitoring</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # -------------------------------
    # FEATURE CARDS (3 COLUMNS)
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class='card'>
                <h3>📡 Real-Time AQI</h3>
                <p>Get live air quality data fetched directly from OpenAQ API.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='card'>
                <h3>📈 Hybrid Forecasting</h3>
                <p>Uses ARIMA + LSTM simulation to predict AQI future trends.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class='card'>
                <h3>⚛ Quantum Computing</h3>
                <p>Runs Qiskit-based quantum circuit simulations (VQC model).</p>
            </div>
        """, unsafe_allow_html=True)


    st.write("")
    st.write("")

    # -------------------------------
    # MORE FEATURES
    # -------------------------------
    st.markdown("""
        <div class='card'>
            <h3>✨ Dashboard Highlights</h3>
            <ul>
                <li>🌬 Live AQI Levels</li>
                <li>📉 Forecast for next 24 hours (AI model simulated)</li>
                <li>🗺 Heatmap of surrounding region</li>
                <li>🚨 Anomaly Detection module (sudden spikes detection)</li>
                <li>⚛ Quantum Variational Circuit visualizer</li>
                <li>🌌 Futuristic Neon Cyber UI + glowing animations</li>
                <li>☁️ Fully deployed on Streamlit Cloud</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------------
    # FOOTER (Dynamic)
    # -------------------------------
    st.markdown(
        f"""
        <p style='color:#55dfff; text-align:center; margin-top:25px;'>
            Last refreshed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </p>
        """,
        unsafe_allow_html=True
    )
