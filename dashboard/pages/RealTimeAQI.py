import streamlit as st
import requests
import json

def run():

    st.markdown("<h2 class='title-glow'>📡 Real-Time Air Quality – Tirupati</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Live AQI data from CPCB / WAQI API</p>", unsafe_allow_html=True)

    CITY = "Tirupati"
    TOKEN = "demo"

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

        # MAIN AQI CARD
        st.markdown(f"""
            <div class='card'>
                <h2>🌬 Current AQI: <span style='color:#00eaff'>{aqi}</span></h2>
                <p>Dominant Pollutant: <b>{dominent.upper()}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")

        # POLLUTANT CARDS
        st.markdown("### 🌫️ Detailed Pollutant Cards")
        st.write("")

        pollutants = []
        for pol, val in iaqi.items():
            pollutants.append({"Pollutant": pol.upper(), "Value": val.get("v", "N/A")})

        col1, col2, col3 = st.columns(3)

        for i, row in enumerate(pollutants):

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

        # -----------------------------------------------------
        # PDF DOWNLOAD
        # -----------------------------------------------------
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        import io

        pdf_buffer = io.BytesIO()
        pdf = canvas.Canvas(pdf_buffer, pagesize=letter)

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 750, f"AQI Report - {CITY}")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 720, f"Current AQI: {aqi}")
        pdf.drawString(50, 700, f"Dominant Pollutant: {dominent.upper()}")

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, 670, "Pollutant Levels:")

        y = 650
        pdf.setFont("Helvetica", 12)
        for p in pollutants:
            pdf.drawString(60, y, f"{p['Pollutant']}: {p['Value']}")
            y -= 20
            if y < 50:
                pdf.showPage()
                pdf.setFont("Helvetica", 12)
                y = 750

        pdf.save()
        pdf_buffer.seek(0)

        st.download_button(
            label="📥 Download AQI Report (PDF)",
            data=pdf_buffer,
            file_name=f"{CITY}_AQI_Report.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"❌ Error fetching AQI: {str(e)}")
