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
            <div class='card' style='margin-bottom:25px;'>
                <h2>🌬 Current AQI: <span style='color:#00eaff'>{aqi}</span></h2>
                <p>Dominant Pollutant: <b>{dominent.upper()}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")

        # TITLE
        st.markdown("### 🌫️ Detailed Pollutant Cards")
        st.write("<br>", unsafe_allow_html=True)

        # POLLUTANT CARDS WITH BETTER SPACING
        # Pollutant Full Names Mapping
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

        # Converting pollutants list
        pollutants = []
        for pol, val in iaqi.items():
            code = pol.upper()
            full_name = POLLUTANT_NAMES.get(code, code)
            pollutants.append({
                "FullName": full_name,
                "Code": code,
                "Value": val.get("v", "N/A")
            })

        # Display cards with full names
        col1, col2, col3 = st.columns(3)

        for i, row in enumerate(pollutants):

            card_html = f"""
                <div class='card' style='margin:15px; padding:20px; border-radius:15px;'>
                    <h4>{row['FullName']}</h4>
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
        # ENHANCED PDF DOWNLOAD
        # -----------------------------------------------------
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors
        import io

        pdf_buffer = io.BytesIO()
        pdf = canvas.Canvas(pdf_buffer, pagesize=letter)

        # HEADER BOX
        pdf.setFillColorRGB(0.1, 0.1, 0.4)
        pdf.rect(0, 740, 600, 50, stroke=0, fill=1)

        pdf.setFillColor(colors.white)
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(20, 760, f"AQI REPORT – {CITY.upper()}")

        # MAIN AQI SECTION
        pdf.setFillColor(colors.black)
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(20, 720, f"Current AQI: {aqi}")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(20, 700, f"Dominant Pollutant: {dominent.upper()}")

        # POLLUTANT SECTION
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(20, 670, "Pollutant Levels:")

        y = 650
        pdf.setFont("Helvetica", 12)
        for p in pollutants:
            pdf.drawString(40, y, f"- {p['Pollutant']}: {p['Value']}")
            y -= 20
            if y < 40:
                pdf.showPage()
                y = 750

        pdf.save()
        pdf_buffer.seek(0)

        # Stylish Download Button
        st.download_button(
            label="⬇️ Download",
            data=pdf_buffer,
            file_name=f"{CITY}_AQI_Report.pdf",
            mime="application/pdf",
            help="Click to download AQI report"
        )

    except Exception as e:
        st.error(f"❌ Error fetching AQI: {str(e)}")
