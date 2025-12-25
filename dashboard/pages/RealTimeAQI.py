import streamlit as st
import requests
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO

def run():

    st.markdown("<h2 class='title-glow'>📡 Real-Time Air Quality – Tirupati</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Live AQI data from WAQI API</p>", unsafe_allow_html=True)

    CITY = "Tirupati"
    TOKEN = "e15cda8309930fc97e17a9e977bd4153d57c5c1a"

    url = f"https://api.waqi.info/feed/{CITY}/?token={TOKEN}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] != "ok":
            st.error("❌ AQI data unavailable. Try again later.")
            return

        # MAIN DATA
        aqi = data["data"]["aqi"]
        dominent = data["data"].get("dominentpol", "N/A")
        iaqi = data["data"].get("iaqi", {})

        # MAIN AQI CARD
        st.markdown(f"""
            <div class='card'>
                <h2>🌬 Current AQI: <span style='color:#00eaff'>{aqi}</span></h2>
                <p>Dominant Pollutant: <b>{dominent.upper()}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("### 🌫️ Detailed Pollutant Cards")
        st.write("")

        # POLLUTANT FULL NAMES
        POLLUTANT_NAMES = {
            "PM25": "Fine Particulate Matter (PM2.5)",
            "PM10": "Coarse Particulate Matter (PM10)",
            "O3": "Ozone (O₃)",
            "NO2": "Nitrogen Dioxide (NO₂)",
            "SO2": "Sulfur Dioxide (SO₂)",
            "CO": "Carbon Monoxide (CO)",
            "T": "Temperature (T)",
            "H": "Humidity (H)",
            "P": "Air Pressure (P)",
            "DEW": "Dew Point (DEW)",
            "W": "Wind Speed (W)"
        }

        # Build pollutant list
        pollutants = []
        for pol, val in iaqi.items():
            code = pol.upper()
            pollutants.append({
                "FullName": POLLUTANT_NAMES.get(code, code),
                "Value": val.get("v", "N/A")
            })

        # DISPLAY CARDS
        cols = st.columns(3)

        for i, item in enumerate(pollutants):
            html = f"""
                <div class='card' style="margin:20px; padding:20px; border-radius:15px;">
                    <h4>{item['FullName']}</h4>
                    <p>Value: <b>{item['Value']}</b></p>
                </div>
            """

            cols[i % 3].markdown(html, unsafe_allow_html=True)

        st.write("")

        # ---------------------------------------------------------
        # PDF DOWNLOAD
        # ---------------------------------------------------------

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph(f"<b>Air Quality Report - {CITY}</b>", styles["Title"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph(f"<b>Current AQI:</b> {aqi}", styles["Heading2"]))
        story.append(Paragraph(f"<b>Dominant Pollutant:</b> {dominent.upper()}", styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Pollutant Levels:</b>", styles["Heading2"]))
        story.append(Spacer(1, 10))

        for item in pollutants:
            story.append(Paragraph(f"{item['FullName']}: <b>{item['Value']}</b>", styles["Normal"]))
            story.append(Spacer(1, 8))

        doc.build(story)
        pdf_data = buffer.getvalue()

        st.download_button(
            label="📄 Download",
            data=pdf_data,
            file_name=f"{CITY}_AQI_Report.pdf",
            mime="application/pdf",
            help="Download the AQI Report as a PDF"
        )

    except Exception as e:
        st.error(f"❌ Error fetching AQI: {str(e)}")
