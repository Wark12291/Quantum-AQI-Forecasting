import streamlit as st
import requests
import pandas as pd

TOKEN = "e15cda8309930fc97e17a9e977bd4153d57c5c1a"

# Top major cities of India
CITIES = [
    "delhi", "mumbai", "kolkata", "chennai", "bangalore", "hyderabad",
    "pune", "ahmedabad", "lucknow", "jaipur", "patna", "kanpur",
    "visakhapatnam", "chandigarh", "bhopal", "indore",
    "nagpur", "surat", "coimbatore", "tirupati"
]

def get_city_aqi(city):
    """Fetch AQI for a single city"""
    try:
        url = f"https://api.waqi.info/feed/{city}/?token={TOKEN}"
        r = requests.get(url).json()
        if r["status"] == "ok":
            return r["data"]["aqi"]
        return None
    except:
        return None


def run():
    st.markdown("<h2 class='title-glow'>🌏 India – Major Cities Air Quality Index</h2>", unsafe_allow_html=True)
    st.write("Fetching real-time AQI…")

    aqi_list = []

    for city in CITIES:
        aqi_value = get_city_aqi(city)
        aqi_list.append({"City": city.title(), "AQI": aqi_value})

    df = pd.DataFrame(aqi_list)

    # Remove None values
    df = df.dropna()

    # Sort by AQI (High → Low)
    df_sorted = df.sort_values(by="AQI", ascending=False)

    # Show top polluted cities
    st.markdown("## 🔥 Top 5 Most Polluted Cities in India")
    st.table(df_sorted.head(5))

    # Show cleanest cities
    st.markdown("## 🌿 Top 5 Cleanest Cities in India")
    st.table(df_sorted.tail(5))

    # Show full data
    st.markdown("## 📊 AQI Levels for All Major Cities")
    st.dataframe(df_sorted.reset_index(drop=True))

    # Cards section
    st.markdown("## 🏙 City AQI Cards")
    cols = st.columns(3)

    for i, row in df_sorted.iterrows():
        html = f"""
            <div class='card' style="padding:20px; margin:15px; border-radius:18px;">
                <h4 style='margin:0; font-size:22px;'>{row['City']}</h4>
                <p style='font-size:18px;'>AQI: <b>{row['AQI']}</b></p>
            </div>
        """
        cols[i % 3].markdown(html, unsafe_allow_html=True)
