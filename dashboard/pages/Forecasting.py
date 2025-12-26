import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Try to import TensorFlow LSTM (fallback if missing)
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    TENSORFLOW_AVAILABLE = True
except:
    TENSORFLOW_AVAILABLE = False


def run():

    st.markdown("<h2 class='title-glow'>📈 AQI Forecasting – LSTM + ARIMA</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Hybrid ML Forecasting for Tirupati Air Quality</p>",
                unsafe_allow_html=True)

    # ----------------------------------------------------------
    # SAMPLE DATA (you can replace with live TTCB/API input)
    # ----------------------------------------------------------
    np.random.seed(42)
    last_60_days = np.abs(np.random.normal(90, 20, 60))  # Fake AQI data
    df = pd.DataFrame({"AQI": last_60_days})

    st.markdown("### 📊 Last 60 Days AQI Trend")
    st.line_chart(df)

    # ----------------------------------------------------------
    # TRAIN ARIMA MODEL
    # ----------------------------------------------------------
    st.subheader("🔮 ARIMA Forecast")

    arima_model = ARIMA(df["AQI"], order=(5, 1, 2))
    arima_fit = arima_model.fit()
    arima_pred = arima_fit.forecast(steps=7)

    # ----------------------------------------------------------
    # OPTIONAL: TRAIN LSTM MODEL (if TensorFlow available)
    # ----------------------------------------------------------
    st.subheader("🤖 LSTM Forecast (Neural Network)")

    if TENSORFLOW_AVAILABLE:
        st.success("TensorFlow detected — LSTM forecast active ✔")

        # Prepare data
        data = df["AQI"].values
        X, y = [], []
        for i in range(len(data) - 5):
            X.append(data[i:i + 5])
            y.append(data[i + 5])

        X = np.array(X).reshape(-1, 5, 1)
        y = np.array(y)

        # LSTM model
        model = Sequential()
        model.add(LSTM(32, activation='tanh', return_sequences=False, input_shape=(5, 1)))
        model.add(Dense(1))
        model.compile(optimizer="adam", loss="mse")
        model.fit(X, y, epochs=10, batch_size=4, verbose=0)

        # Forecast next 7 days
        lstm_input = data[-5:].reshape(1, 5, 1)
        lstm_pred = []
        for _ in range(7):
            next_val = model.predict(lstm_input)[0][0]
            lstm_pred.append(next_val)
            lstm_input = np.append(lstm_input.flatten()[1:], next_val).reshape(1, 5, 1)

        lstm_pred = np.array(lstm_pred)

    else:
        st.warning("TensorFlow not installed — using ARIMA only.")
        lstm_pred = None

    # ----------------------------------------------------------
    # SHOW FORECAST
    # ----------------------------------------------------------
    st.markdown("### 📅 7-Day AQI Forecast Results")

    forecast_df = pd.DataFrame({
        "Day": [f"Day {i+1}" for i in range(7)],
        "ARIMA_Prediction": np.round(arima_pred, 2),
        "LSTM_Prediction": np.round(lstm_pred, 2) if lstm_pred is not None else "N/A"
    })

    st.dataframe(forecast_df)

    # ----------------------------------------------------------
    # CHART VISUALIZATION
    # ----------------------------------------------------------
    st.markdown("### 📈 Forecast Visualization (Neon Style)")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df["AQI"], label="Actual AQI", color="#00eaff")
    ax.plot(range(60, 67), arima_pred, label="ARIMA Forecast", color="#ff007f")

    if lstm_pred is not None:
        ax.plot(range(60, 67), lstm_pred, label="LSTM Forecast", color="#00ff88")

    ax.set_facecolor("#0b0f19")
    fig.patch.set_facecolor("#0b0f19")
    ax.grid(True, color="#1f2a40")
    ax.legend(facecolor="#111827", labelcolor="white")

    st.pyplot(fig)

    st.info("✨ Hybrid Forecast Complete – ARIMA + LSTM Model Ready.")


