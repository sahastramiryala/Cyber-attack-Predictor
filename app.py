import streamlit as st
import datetime
import random
import matplotlib.pyplot as plt

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="Cyber Attack Prediction System",
    layout="wide"
)

# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
st.sidebar.title("🔐 Cyber Security Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Prediction System",
        "Analytics Dashboard",
        "Attack Information",
        "User Monitor"
    ]
)

# =========================================================
# 1️⃣ PREDICTION SYSTEM PAGE
# =========================================================
if page == "Prediction System":

    st.title("🚨 Real-Time Cyber Attack Prediction")

    col1, col2 = st.columns(2)

    with col1:
        duration = st.number_input("Duration", 0.0)
        src_bytes = st.number_input("Source Bytes", 0.0)
        dst_bytes = st.number_input("Destination Bytes", 0.0)

        predict_button = st.button("🔍 Predict")

    if predict_button:

        # Example logic (Replace later with your ML model)
        if src_bytes > 10000:
            result = "🚨 Attack Detected"
            attack_type = random.choice(
                ["DDoS", "DoS", "Probe", "R2L", "U2R"]
            )
        else:
            result = "✅ Normal Traffic"
            attack_type = "None"

        timestamp = datetime.datetime.now()
        user_id = random.randint(1000, 9999)
        network = random.choice(["WiFi", "LAN", "Public Network"])

        st.subheader("🔎 Prediction Output")

        if "Attack" in result:
            st.error(result)
            st.warning(f"Attack Type: {attack_type}")
            st.info(f"User ID: {user_id}")
            st.info(f"Network Type: {network}")
            st.write("Timestamp:", timestamp)

            st.markdown("### ⚠️ Precautions")
            st.write("""
            - Enable Firewall Immediately
            - Block Suspicious IP Address
            - Monitor Traffic Logs
            - Enable Intrusion Detection System
            - Reset Compromised Credentials
            """)

            # Sound Alert
            st.audio("alert.mp3")

        else:
            st.success(result)

# =========================================================
# 2️⃣ ANALYTICS DASHBOARD
# =========================================================
if page == "Analytics Dashboard":

    st.title("📊 Model Accuracy Comparison")

    models = ["ML Model", "ML + GAN Model"]
    accuracy = [85, 93]

    # Bar Chart
    fig1, ax1 = plt.subplots()
    ax1.bar(models, accuracy)
    ax1.set_ylabel("Accuracy %")
    st.pyplot(fig1)

    # Pie Chart
    fig2, ax2 = plt.subplots()
    ax2.pie(accuracy, labels=models, autopct='%1.1f%%')
    st.pyplot(fig2)

    # Line Graph
    fig3, ax3 = plt.subplots()
    ax3.plot(models, accuracy, marker='o')
    st.pyplot(fig3)

    # Scatter Plot
    fig4, ax4 = plt.subplots()
    ax4.scatter(models, accuracy)
    st.pyplot(fig4)

# =========================================================
# 3️⃣ ATTACK INFORMATION PAGE
# =========================================================
if page == "Attack Information":

    st.title("📚 Types of Cyber Attacks")

    attacks = {
        "DDoS": "Distributed Denial of Service attack floods a server with massive traffic.",
        "DoS": "Denial of Service attack disrupts normal service.",
        "Probe": "Scanning attack used to find system vulnerabilities.",
        "R2L": "Remote to Local attack gains local access from remote machine.",
        "U2R": "User to Root attack escalates privileges to root level."
    }

    for attack, info in attacks.items():
        st.subheader(attack)
        st.write(info)

# =========================================================
# 4️⃣ USER MONITOR PAGE
# =========================================================
if page == "User Monitor":

    st.title("👤 User Monitoring Panel")

    st.write("Attacker ID: 4587")
    st.write("Network Type: Public WiFi")
    st.write("Attack Type: DDoS")
    st.write("Timestamp:", datetime.datetime.now())