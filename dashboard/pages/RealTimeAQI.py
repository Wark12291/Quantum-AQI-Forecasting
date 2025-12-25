import streamlit as st
import requests
import pandas as pd

def run():

    st.markdown("<h2 class='title-glow'>📡 Real-Time Air Quality – Tirupati</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Live AQI data from CPCB / WAQI API</p>", unsafe_allow_html=True)

    CITY = "Tirupati"
    TOKEN = "e15cda8309930fc97e17a9e977bd4153d57c5c1a"   # Replace with your API key later

    url = f"https://api.waqi.info/feed/{CITY}/?token={TOKEN}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] != "ok":
            st.error("❌ AQI data unavailable. Try again later.")
            return

        aqi = data["data"]["aqi"]
        dominent = data["data"].get("dominentpol", "N/A")
        iaqi = data["data"].get("iaqi", {})

        # Display main AQI
        st.markdown(f"""
            <div class='card'>
                <h2>🌬 Current AQI: <span style='color:#00eaff'>{aqi}</span></h2>
                <p>Dominant Pollutant: <b>{dominent.upper()}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("### 📊 Pollutant Levels")

        # Extract pollutants
        pollutant_data = []
        for pol, val in iaqi.items():
            pollutant_data.append([pol.upper(), val.get("v", "N/A")])

        df = pd.DataFrame(pollutant_data, columns=["Pollutant", "Value"])
        st.dataframe(df, use_container_width=True)

        # Display pollutant cards
        st.markdown("### 🌫️ Detailed Pollutant Cards")
        col1, col2, col3 = st.columns(3)

        for i, row in df.iterrows():
            card_html = f"""
                <div class='card'>
                    <h4>{row['Pollutant']}</h4>
                    <p>Value: <b>{row['Value']}</b></p>
                </div>
            """

            if i % 3 == 0:
                col1.markdown(card_html, unsafe_allow_html=True)
            elif i % 3 == 1:
                col2.markdown(card_html, unsafe_allow_html=True)
            else:
                col3.markdown(card_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error fetching data: {str(e)}")
