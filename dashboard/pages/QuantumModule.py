import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---- Quantum Imports ----
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    QISKIT_AVAILABLE = True
except:
    QISKIT_AVAILABLE = False


def run():

    st.markdown("<h2 class='title-glow'>🧠 Quantum Pollution Simulation</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Quantum-inspired uncertainty modeling using AerSimulator</p>",
                unsafe_allow_html=True)

    if not QISKIT_AVAILABLE:
        st.error("❌ Qiskit is not installed. Add 'qiskit' to requirements.txt")
        return

    st.markdown("---")

    st.markdown("### ⚙️ Quantum Circuit – Atmospheric Noise Simulation")

    # Environmental randomness (user-controlled)
    theta = st.slider("Environmental Fluctuation (θ)", 0.0, 3.14, 1.2, 0.01)

    # -------------------------------
    # Quantum Simulation
    # -------------------------------
    qc = QuantumCircuit(1, 1)
    qc.h(0)              # base uncertainty
    qc.rx(theta, 0)      # environmental rotation
    qc.measure(0, 0)

    sim = AerSimulator()
    result = sim.run(qc, shots=1000).result()
    counts = result.get_counts()

    # Compute probabilities
    high_prob = counts.get('1', 0) / 1000  # higher pollution
    low_prob = counts.get('0', 0) / 1000   # lower pollution

    # Convert probability → AQI
    quantum_aqi = round(50 + high_prob * 250, 2)  # scale: 50→300

    # Noise Level
    noise_level = round(abs(np.sin(theta)), 2)

    # -------------------------------
    # Display Neon Output Cards
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
        <div class='card' style="padding:25px; border-radius:18px;">
            <h3>🔮 High Pollution Probability</h3>
            <h2 style='color:#00eaff'>{round(high_prob*100,2)}%</h2>
        </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
        <div class='card' style="padding:25px; border-radius:18px;">
            <h3>🌫 Quantum Simulated AQI</h3>
            <h2 style='color:#00ff88'>{quantum_aqi}</h2>
        </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
        <div class='card' style="padding:25px; border-radius:18px;">
            <h3>🔉 Environmental Noise Level</h3>
            <h2 style='color:#ff007f'>{noise_level}</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # -------------------------------
    # Probability Bar Chart
    # -------------------------------
    st.markdown("### 📊 Quantum State Probability Distribution")

    fig, ax = plt.subplots(figsize=(5,3))
    ax.bar(["Low (|0⟩)", "High (|1⟩)"], [low_prob, high_prob])
    ax.set_ylabel("Probability")
    ax.set_ylim(0,1)

    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#0b0f19")
    ax.tick_params(colors="white")
    ax.yaxis.label.set_color("white")

    for spine in ax.spines.values():
        spine.set_edgecolor("white")

    st.pyplot(fig)

    # -------------------------------
    # Detailed Table
    # -------------------------------
    st.markdown("### 🔍 Quantum State Breakdown")

    st.table({
        "Quantum State": ["|0⟩ – Low Pollution", "|1⟩ – High Pollution"],
        "Probability": [f"{round(low_prob*100,2)}%", f"{round(high_prob*100,2)}%"]
    })

    st.markdown("---")

    st.info("""
    **Interpretation:**
    - Quantum circuits model atmospheric randomness.
    - |1⟩ is mapped to higher pollution probability.
    - Noise level influences AQI fluctuations.
    - This provides a quantum-inspired stochastic pollution estimate.
    """)

