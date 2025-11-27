# app.py
# AetherVision Omega – HyperCity GeoAI SmartCity System
# Streamlit app connecting all 8 branches

import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# BASIC CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AetherVision Omega – HyperCity GeoAI",
    layout="wide"
)

BASE = Path(__file__).parent

def read_text(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    return f"[Missing file: {path}]"

def read_html(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    return f"<h4>Missing file: {path}</h4>"

def read_csv(path: Path):
    if path.exists():
        try:
            return pd.read_csv(path)
        except Exception:
            return None
    return None

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("AetherVision Omega")
section = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "1️⃣ Branch 1 – Digital Twin",
        "2️⃣ Branch 2 – Environmental Analytics",
        "3️⃣ Branch 3 – GeoAI Fusion Engine",
        "4️⃣ Branch 4 – Real-Time Risk Model",
        "5️⃣ Branch 5 – 7-Day Hazard Forecast",
        "6️⃣ Branch 6 – GeoHealth Dashboard",
        "7️⃣ Branch 7 – Early Warning Alerts",
        "8️⃣ Branch 8 – SmartCity Decision Engine",
    ]
)

# --------------------------------------------------
# HOME
# --------------------------------------------------
if section == "🏠 Home":
    st.title("AetherVision Omega – HyperCity GeoAI SmartCity System")

    st.markdown(
        """
        **AetherVision Omega** is an 8-branch GeoAI system that:

        - Builds a digital twin of Indian cities  
        - Maps pollution, geology, climate and health risk  
        - Computes multi-hazard risk scores  
        - Forecasts hazards for the next days  
        - Generates early warning alerts  
        - Produces final SmartCity recommendations  

        Use the sidebar to explore each branch.
        """
    )

    st.subheader("System Architecture (8 Branches)")
    st.markdown(
        """
        1. Branch 1 – Core Digital Twin  
        2. Branch 2 – Environmental Analytics  
        3. Branch 3 – GeoAI Fusion Engine  
        4. Branch 4 – Real-Time Risk Model  
        5. Branch 5 – Urban Hazard Forecasting  
        6. Branch 6 – City GeoHealth Dashboard  
        7. Branch 7 – Early Warning Alerts (48 hrs)  
        8. Branch 8 – SmartCity Decision Engine  
        """
    )

# --------------------------------------------------
# BRANCH 1 – DIGITAL TWIN
# --------------------------------------------------
elif section == "1️⃣ Branch 1 – Digital Twin":
    st.title("Branch 1 – Core GeoAI Digital Twin")

    # Adjust this folder name if different in your repo
    branch1_dir = BASE / "branch-1-core-digital-twin"

    st.write("Folder:", branch1_dir)

    maps = {
        "Digital Twin Base": "digital_twin_base.html",
        "Environmental Layers": "india_env_layers.html",
        "Geology Layers": "geology_layers.html",
        "SmartCity Climate Layers": "omega_smartcity.html",
        "Fusion Risk Map": "fusion_risk_map.html",
        "Full Dashboard": "omega_dashboard.html",
    }

    map_choice = st.selectbox("Select map", list(maps.keys()))

    # Either all HTMLs are directly in branch1_dir,
    # or inside a subfolder like AetherVision_Omega_Branch1_Outputs
    html_path = branch1_dir / maps[map_choice]
    if not html_path.exists():
        html_path = branch1_dir / "AetherVision_Omega_Branch1_Outputs" / maps[map_choice]

    st.subheader(map_choice)
    html_content = read_html(html_path)
    st.components.v1.html(html_content, height=600, scrolling=True)

# --------------------------------------------------
# BRANCH 2 – ENVIRONMENTAL ANALYTICS
# --------------------------------------------------
elif section == "2️⃣ Branch 2 – Environmental Analytics":
    st.title("Branch 2 – Environmental & Pollution Analytics")

    branch2_dir = BASE / "branch-2-environmental-analytics"
    methodology = branch2_dir / "methodology.md"
    summary = branch2_dir / "summary_report.md"

    st.subheader("Methodology")
    st.markdown(read_text(methodology))

    st.subheader("Summary Report")
    st.markdown(read_text(summary))

# --------------------------------------------------
# BRANCH 3 – GEOAI FUSION ENGINE
# --------------------------------------------------
elif section == "3️⃣ Branch 3 – GeoAI Fusion Engine":
    st.title("Branch 3 – GeoAI Fusion Engine")

    branch3_dir = BASE / "branch-3-geoai-fusion-engine"
    fusion_html = branch3_dir / "fusion_risk_heatmap.html"
    fusion_csv = branch3_dir / "fusion_risk_scores.csv"

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Fusion Risk Heatmap")
        html_content = read_html(fusion_html)
        st.components.v1.html(html_content, height=600, scrolling=True)

    with col2:
        st.subheader("Fusion Risk Scores")
        df = read_csv(fusion_csv)
        if df is not None:
            st.dataframe(df)
        else:
            st.info("fusion_risk_scores.csv not found")

# --------------------------------------------------
# BRANCH 4 – REAL-TIME RISK MODEL
# --------------------------------------------------
elif section == "4️⃣ Branch 4 – Real-Time Risk Model":
    st.title("Branch 4 – Real-Time GeoAI Risk Engine")

    branch4_dir = BASE / "branch-4-realtime-risk-model"
    risk_html = branch4_dir / "risk_map.html"
    risk_csv = branch4_dir / "risk_scores.csv"
    hazard_report = branch4_dir / "hazard_report.txt"

    st.subheader("Risk Heatmap")
    html_content = read_html(risk_html)
    st.components.v1.html(html_content, height=600, scrolling=True)

    st.subheader("Risk Scores Table")
    df = read_csv(risk_csv)
    if df is not None:
        st.dataframe(df)
    else:
        st.info("risk_scores.csv not found")

    st.subheader("Hazard Report")
    st.text(read_text(hazard_report))

# --------------------------------------------------
# BRANCH 5 – 7-DAY HAZARD FORECAST
# --------------------------------------------------
elif section == "5️⃣ Branch 5 – 7-Day Hazard Forecast":
    st.title("Branch 5 – 7-Day Urban Hazard Forecasting")

    branch5_dir = BASE / "branch-5-hazard-forecasting-engine"
    forecast_html = branch5_dir / "forecast_heatmap.html"
    forecast_csv = branch5_dir / "forecast_with_scores.csv"
    forecast_report = branch5_dir / "forecast_report.txt"

    st.subheader("Forecast Heatmap (Latest Day)")
    html_content = read_html(forecast_html)
    st.components.v1.html(html_content, height=600, scrolling=True)

    st.subheader("Forecast With Scores")
    df = read_csv(forecast_csv)
    if df is not None:
        st.dataframe(df)
    else:
        st.info("forecast_with_scores.csv not found")

    st.subheader("Forecast Summary Report")
    st.text(read_text(forecast_report))

# --------------------------------------------------
# BRANCH 6 – CITY GEOHEALTH DASHBOARD
# --------------------------------------------------
elif section == "6️⃣ Branch 6 – GeoHealth Dashboard":
    st.title("Branch 6 – City GeoHealth Dashboard")

    branch6_dir = BASE / "branch-6-city-geohealth-dashboard"
    geo_html = branch6_dir / "geohealth_dashboard.html"
    geo_csv = branch6_dir / "geohealth_dataset.csv"
    geo_report = branch6_dir / "geohealth_report.txt"

    st.subheader("GeoHealth Risk Map")
    html_content = read_html(geo_html)
    st.components.v1.html(html_content, height=600, scrolling=True)

    st.subheader("GeoHealth Dataset")
    df = read_csv(geo_csv)
    if df is not None:
        st.dataframe(df)
    else:
        st.info("geohealth_dataset.csv not found")

    st.subheader("GeoHealth Summary Report")
    st.text(read_text(geo_report))

# --------------------------------------------------
# BRANCH 7 – EARLY WARNING ALERTS
# --------------------------------------------------
elif section == "7️⃣ Branch 7 – Early Warning Alerts":
    st.title("Branch 7 – Early Warning Disaster Alert Engine")

    branch7_dir = BASE / "branch-7-early-warning-alerts"
    realtime_csv = branch7_dir / "realtime_hazard_data.csv"
    alerts_csv = branch7_dir / "disaster_alerts_48hrs.csv"
    alerts_report = branch7_dir / "alert_report.txt"

    st.subheader("Disaster Alerts (48 hours)")
    df_alerts = read_csv(alerts_csv)
    if df_alerts is not None:
        st.dataframe(df_alerts)
    else:
        st.info("disaster_alerts_48hrs.csv not found")

    st.subheader("Raw 48-hour Hazard Data (First 100 rows)")
    df_rt = read_csv(realtime_csv)
    if df_rt is not None:
        st.dataframe(df_rt.head(100))
    else:
        st.info("realtime_hazard_data.csv not found")

    st.subheader("Alert Summary Report")
    st.text(read_text(alerts_report))

# --------------------------------------------------
# BRANCH 8 – SMARTCITY DECISION ENGINE
# --------------------------------------------------
elif section == "8️⃣ Branch 8 – SmartCity Decision Engine":
    st.title("Branch 8 – Autonomous SmartCity Decision Engine")

    branch8_dir = BASE / "branch-8-smartcity-decision-engine"
    decision_csv = branch8_dir / "smartcity_decision_engine.csv"
    decision_report = branch8_dir / "smartcity_recommendation_report.txt"

    st.subheader("SmartCity Decision Table")
    df = read_csv(decision_csv)
    if df is not None:
        st.dataframe(df)
    else:
        st.info("smartcity_decision_engine.csv not found")

    st.subheader("AI Recommendation Report")
    st.text(read_text(decision_report))
