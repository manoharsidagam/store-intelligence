import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# =====================================
# AUTO REFRESH
# =====================================
st_autorefresh(interval=5000, key="dashboard_refresh")

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)
st.markdown("""
<style>

/* Metric Cards */

div[data-testid="metric-container"] {

    background-color: white;

    border: 1px solid #E5E7EB;

    padding: 15px;

    border-radius: 12px;

    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* Main */

.block-container {

    padding-top: 2rem;
}

/* Section Headers */

h2 {

    color: #2563EB;
}

/* Dataframes */

[data-testid="stDataFrame"] {

    border-radius: 12px;
}

/* Sidebar */

section[data-testid="stSidebar"] {

    background-color: #F8FAFC;
}

</style>
""", unsafe_allow_html=True)

st.title("🏪 Multi-Store Intelligence Dashboard")

st.caption("Powered by YOLOv8 + ByteTrack + FastAPI + Streamlit")

# =====================================
# API DATA
# =====================================

store1 = requests.get(
    "http://127.0.0.1:8000/stores/store_1/metrics"
).json()

store2 = requests.get(
    "http://127.0.0.1:8000/stores/store_2/metrics"
).json()

events = requests.get(
    "http://127.0.0.1:8000/events"
).json()

anomalies = requests.get(
    "http://127.0.0.1:8000/anomalies"
).json()

# =====================================
# SYSTEM STATUS PANEL
# =====================================

st.sidebar.title("⚙️ System Status")

st.sidebar.success("✅ API Online")

st.sidebar.info(
    f"📋 Events Loaded: {len(events)}"
)

st.sidebar.info(
    f"🚨 Active Anomalies: {len(anomalies)}"
)

st.sidebar.success("✅ Dashboard Live")


st.sidebar.subheader("🕒 Last Refresh")

st.sidebar.write(
    pd.Timestamp.now().strftime("%H:%M:%S")
)
st.sidebar.divider()

st.sidebar.subheader("📡 API Monitoring")

st.sidebar.metric(
    "Stores",
    2
)
# =====================================
# EXECUTIVE KPI
# =====================================

total_visitors = (
    store1["entries"] +
    store2["entries"]
)

total_occupancy = (
    store1["occupancy"] +
    store2["occupancy"]
)

total_purchases = (
    store1["purchases"] +
    store2["purchases"]
)

overall_conversion = round(
    (
        total_purchases /
        max(total_visitors, 1)
    ) * 100,
    2
)

active_anomalies = len(anomalies)

health_score = max(
    100 - (active_anomalies * 10),
    0
)

k1, k2, k3, k4, k5, k6 = st.columns(6)

k1.metric("👥 Total Visitors", total_visitors)
k2.metric("🏬 Occupancy", total_occupancy)
k3.metric("🎯 Conversion %", overall_conversion)
k4.metric("🛒 Purchases", total_purchases)
k5.metric("🚨 Anomalies", active_anomalies)
k6.metric("💚 Health Score", f"{health_score}%")

st.divider()

# =====================================
# STORE PERFORMANCE
# =====================================
col1,col2 = st.columns(2)

with col1:

    st.subheader("🏬 Store 1")

    st.metric("👥 Visitors", store1["entries"])
    st.metric("🏬 Occupancy", store1["occupancy"])
    st.metric("🛒 Purchases", store1["purchases"])
    st.metric("🎯 Conversion", f"{store1['conversion_rate']}%")

    health1 = 90

    st.progress(health1/100)

    st.caption(f"Health Score : {health1}%")

with col2:

    st.subheader("🏬 Store 2")

    st.metric("👥 Visitors", store2["entries"])
    st.metric("🏬 Occupancy", store2["occupancy"])
    st.metric("🛒 Purchases", store2["purchases"])
    st.metric("🎯 Conversion", f"{store2['conversion_rate']}%")

    health2 = 95

    st.progress(health2/100)

    st.caption(f"Health Score : {health2}%")
# =====================================
# FUNNEL CHARTS
# =====================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Store 1 Conversion Funnel")

    funnel1 = pd.DataFrame({
        "Stage": [
            "Entry",
            "Billing",
            "Purchase"
        ],
        "Count": [
            store1["entries"],
            store1["billing_visitors"],
            store1["purchases"]
        ]
    })

    fig1 = px.funnel(
        funnel1,
        x="Count",
        y="Stage",
        title="Store 1 Funnel"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    st.subheader("📊 Store 2 Conversion Funnel")

    funnel2 = pd.DataFrame({
        "Stage": [
            "Entry",
            "Billing",
            "Purchase"
        ],
        "Count": [
            store2["entries"],
            store2["billing_visitors"],
            store2["purchases"]
        ]
    })

    fig2 = px.funnel(
        funnel2,
        x="Count",
        y="Stage",
        title="Store 2 Funnel"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =====================================
# HEALTH LEADERBOARD
# =====================================
st.subheader("🏆 Store Health Leaderboard")

store1_health = max(
    100
    - (10 if store1["conversion_rate"] < 30 else 0)
    - (10 if store1["occupancy"] > 5 else 0),
    0
)

store2_health = max(
    100
    - (10 if store2["conversion_rate"] < 30 else 0)
    - (10 if store2["occupancy"] > 5 else 0),
    0
)

leaderboard = pd.DataFrame([
    ["🥇" if store1_health > store2_health else "🥈",
     "Store 1",
     store1_health],

    ["🥇" if store2_health > store1_health else "🥈",
     "Store 2",
     store2_health]
], columns=["Rank", "Store", "Health Score"])

st.dataframe(
    leaderboard,
    use_container_width=True
)

# =====================================
# AI INSIGHTS
# =====================================

best_store = (
    "Store 1"
    if store1["conversion_rate"] >
       store2["conversion_rate"]
    else "Store 2"
)

st.subheader("🤖 AI Business Insights")

st.info(
    f"""
🏆 Best Performing Store: {best_store}

📈 Total Visitors: {total_visitors}

🛒 Total Purchases: {total_purchases}

🚨 Active Anomalies: {active_anomalies}

💡 Recommendation:
Increase billing-zone engagement to improve conversion rate.
"""
)
st.subheader("📋 Executive Summary")

st.success(
    f"""
Total Visitors: {total_visitors}

Total Purchases: {total_purchases}

Best Store: {best_store}

Health Score: {health_score}%

Active Alerts: {active_anomalies}
"""
)

# =====================================
# BUSINESS RECOMMENDATIONS
# =====================================

st.subheader("💡 Smart Recommendations")

if store1["conversion_rate"] < 30:
    st.warning(
        "Store 1: Low conversion detected. Improve billing-zone engagement."
    )

if store2["occupancy"] > 3:
    st.warning(
        "Store 2: High occupancy detected. Consider opening an additional billing counter."
    )

if active_anomalies > 0:
    st.error(
        f"{active_anomalies} active anomalies require attention."
    )

if active_anomalies == 0:
    st.success(
        "All stores operating normally."
    )

st.divider()

st.subheader("🔥 Anomaly Heatmap")

if len(anomalies) > 0:

    heatmap_df = pd.DataFrame(anomalies)

    heatmap_df["score"] = 1

    fig_heat = px.density_heatmap(
        heatmap_df,
        x="store_id",
        y="type",
        z="score",
        title="Anomaly Distribution"
    )

    st.plotly_chart(
        fig_heat,
        use_container_width=True
    )

else:
    st.success("No anomalies available")
# =====================================
# ANOMALIES
# =====================================

st.divider()

st.subheader("🚨 Active Anomalies")

if len(anomalies) == 0:
    st.success("No active anomalies detected")
else:
    for item in anomalies:
        st.warning(
            f"{item['store_id']} | "
            f"{item['type']} | "
            f"Severity: {item['severity']}"
        )

# =====================================
# EVENTS
# =====================================

st.divider()

st.subheader("📋 Recent Events")

df = pd.DataFrame(events)

st.dataframe(
    df,
    use_container_width=True
)

st.success(
    "Real-time Store Monitoring Active ✅"
)