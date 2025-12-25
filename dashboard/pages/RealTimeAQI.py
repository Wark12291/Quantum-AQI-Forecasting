# PREMIUM NEON DOWNLOAD BUTTON
st.markdown("""
    <style>
        .download-btn {
            background: linear-gradient(90deg, #00eaff, #008cff);
            padding: 12px 25px;
            border-radius: 12px;
            color: white !important;
            font-size: 18px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            box-shadow: 0px 0px 12px #00bfff;
            transition: 0.3s;
        }
        .download-btn:hover {
            box-shadow: 0px 0px 25px #00eaff;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

st.download_button(
    label="𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝",
    data=pdf_data,  # FIXED: Changed from data-pdf_data to data=pdf_data
    file_name=f"{CITY}_AQI_Report.pdf",
    mime="application/pdf",
    help="Download the premium AQI Report",
    key="premium_pdf",
)
