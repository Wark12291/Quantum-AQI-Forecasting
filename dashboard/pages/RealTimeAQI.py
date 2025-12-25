import streamlit as st
import requests
import pandas as pd

def run():

    st.markdown("<h2 class='title-glow'>📡 Real-Time Air Quality – Tirupati</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Live AQI data from OpenAQ API</p>", unsafe_allow_html=True)

    # API Endpoint
    url = "https://api.openaq.org/v2/latest?city=Tirupati&limit=10"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            st.error("❌ Could not fetch AQI data from API.")
            return

        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            st.warning("⚠ No AQI sensors available in Tirupati right now.")
            return

        # Extract measurements
        sensors = data["results"][0]
        measurements = sensors["measurements"]

        df = pd.DataFrame(measurements)

        # Display dataframe
        st.markdown("### 📊 Raw Data Table")
        st.dataframe(df, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Cards layout
        st.markdown("### 🌬️ Pollutant Indicators")
        col1, col2, col3 = st.columns(3)

        for index, row in df.iterrows():

            card_html = f"""
                <div class='card' style='margin-bottom:20px;'>
                    <h4>{row['parameter'].upper()}</h4>
                    <p>Value: <b>{row['value']} {row['unit']}</b></p>
                    <p>Last Updated: {row['lastUpdated']}</p>
                </div>
            """

            if index % 3 == 0:
                col1.markdown(card_html, unsafe_allow_html=True)
            elif index % 3 == 1:
                col2.markdown(card_html, unsafe_allow_html=True)
            else:
                col3.markdown(card_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error fetching data: {str(e)}")
