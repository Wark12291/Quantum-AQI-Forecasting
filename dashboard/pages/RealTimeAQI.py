def run():
    import streamlit as st
    import requests
    from reportlab.platypus import *
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from io import BytesIO

    st.markdown("<h2 class='title-glow'>📡 Real-Time Air Quality – Tirupati</h2>", unsafe_allow_html=True)

    CITY = "tirupati"
    TOKEN = "e15cda8309930fc97e17a9e977bd4153d57c5c1a"
    url = f"https://api.waqi.info/feed/{CITY}/?token={TOKEN}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data["status"] != "ok":
            st.error("❌ AQI unavailable")
            return

        aqi = data["data"]["aqi"]
        dominent = data["data"].get("dominentpol", "N/A")
        iaqi = data["data"].get("iaqi", {})

        st.markdown(f"<div class='card'><h2>🌬 AQI: <span style='color:#00eaff'>{aqi}</span></h2><p>Dominant: <b>{dominent}</b></p></div>", unsafe_allow_html=True)

        POLLUTANT_NAMES = {
            "PM25":"Fine Particulate Matter (PM2.5)",
            "PM10":"Coarse Particulate Matter (PM10)",
            "O3":"Ozone (O₃)",
            "NO2":"Nitrogen Dioxide (NO₂)",
            "SO2":"Sulfur Dioxide (SO₂)",
            "CO":"Carbon Monoxide (CO)",
            "T":"Temperature (T)",
            "H":"Humidity (H)",
            "P":"Air Pressure (P)",
            "DEW":"Dew Point (DEW)",
            "W":"Wind Speed (W)"
        }

        pollutants=[]
        for k,v in iaqi.items():
            pollutants.append([POLLUTANT_NAMES.get(k.upper(),k), str(v.get('v','N/A'))])

        cols=st.columns(3)
        for i,item in enumerate(pollutants):
            cols[i%3].markdown(f"<div class='card' style='padding:20px;margin:20px'><h4>{item[0]}</h4><p>Value: <b>{item[1]}</b></p></div>",unsafe_allow_html=True)

        buffer=BytesIO()
        doc=SimpleDocTemplate(buffer,pagesize=letter)
        styles=getSampleStyleSheet()
        story=[]

        story.append(Paragraph(f"AQI Report - Tirupati", ParagraphStyle("t",fontSize=22,textColor=colors.blue,alignment=1)))
        story.append(Spacer(1,15))
        story.append(Paragraph(f"AQI: {aqi}", styles["Normal"]))
        story.append(Paragraph(f"Dominant Pollutant: {dominent}", styles["Normal"]))
        story.append(Spacer(1,15))

        table=Table([["Pollutant","Value"]]+pollutants)
        table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#00bfff")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("GRID",(0,0),(-1,-1),0.5,colors.blue)
        ]))
        story.append(table)
        doc.build(story)
        pdf_data=buffer.getvalue()

        st.download_button("📄 Download", pdf_data, f"{CITY}_AQI_Report.pdf", "application/pdf")

    except Exception as e:
        st.error(f"❌ Error fetching AQI: {str(e)}")
