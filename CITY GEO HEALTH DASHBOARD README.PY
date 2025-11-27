City GeoHealth Dashboard

AetherVision Omega — Environmental & Public Health Intelligence Module


---

📌 Overview

The City GeoHealth Dashboard integrates environmental pollution, climate stress, water quality, and population density to generate a health-focused risk map for major Indian cities.
It converts raw environmental values into a clear Health Risk Score and visualizes the results on an interactive GeoHealth map.

This module helps identify which cities are at greatest public health risk, and why.


---

🎯 Key Features

🔹 All-India Coverage (40+ major cities included)

🔹 Real-time GeoHealth Scoring (AQI, heat index, water quality, density)

🔹 Interactive Dashboard (HTML)

🔹 Complete Dataset (CSV)

🔹 Human-readable Health Report (TXT)

🔹 Color-coded markers for risk levels

🔹 Heatmap showing high-impact zones



---

🧠 How the Engine Works

The GeoHealth Engine evaluates four core indicators:

1. AQI – Air Pollution

Higher values → higher respiratory health risk.

2. Heat Index

Temperature + humidity → heat stress risk.

3. Water Quality Index

Lower values → poorer sanitation and health.

4. Population Density

Densely populated areas experience stronger impacts.


---

🧮 Health Risk Formula

A weighted model generates one final Health Risk Score:

Health Risk Score =
(AQI × 0.40) +
(Heat Stress × 0.20) +
(Water Quality Inverted × 0.20) +
(Population Density × 0.20)

Risk Levels

Severe

High

Moderate

Low



---

📁 Files Generated

This branch outputs:

File	Description

geohealth_dashboard.html	Interactive India-wide health risk map
geohealth_dataset.csv	Full dataset of AQI, heat, water, density & risk
geohealth_report.txt	Organized text summary for judges
CITY_GEOHEALTH_DASHBOARD.ipynb	Core notebook for calculations



---

📊 Dashboard Features

The interactive dashboard includes:

Heatmap of health risk scores

City markers with popups

Color-coded risk levels:

Green → Low

Orange → Moderate

Red → High

Dark Red → Severe


Full health profile per city



---

🛠️ Tech Stack

Python

Pandas

NumPy

Folium

HTML Interactive Maps



---

🎤 How to Present to Judges

Judges will open:

geohealth_dashboard.html → Visual map

geohealth_report.txt → Summary

geohealth_dataset.csv → Data proof


You can say:

> “This module combines climate, pollution, water and population data to show
how environmental pressure directly affects public health.
It reveals which cities are at highest risk and why.”




---

🚀 Why Branch 6 is Important

Shows real environment–health linkage

Easy to understand visually

Uses solid AI scoring

Covers 5 major smart city themes

Perfect for presentation and scoring



---
