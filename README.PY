🌩️ URBAN HAZARD FORECASTING ENGINE

AetherVision Omega – Branch 5

The Urban Hazard Forecasting Engine predicts environmental hazards for the next 7 days using AI-based risk scoring.
It analyzes multiple factors like humidity, pollution, temperature, and wind speed to calculate daily hazard levels and generate forecast maps.


---

📌 Key Features

7-Day Hazard Forecasting for any city

AI-based weighted risk scoring

Interactive Heatmap (HTML)

Complete Forecast Report (TXT)

Structured Forecast Data (CSV)

Clean ZIP Package for Hackathon Submission



---

🧠 How It Works

The forecasting engine uses four environmental variables:

Temperature

Humidity

Air Pollution

Wind Speed


Each factor is given a weight based on real hazard contribution.
A final hazard score is calculated (0–1 scale) for each day.

> Higher score → higher risk day.



All results are saved automatically.


---

📂 Output Files (Included in ZIP)

Your hazard_engine_outputs.zip contains:

1. 7_day_hazard_forecast.csv
Clean daily forecast with all values.


2. forecast_with_scores.csv
Extended sheet with AI risk score.


3. forecast_heatmap.html
Interactive hazard map (visual).


4. forecast_report.txt
Simple text summary for judges.


5. hazard_engine_outputs.zip
Final bundled submission.




---

🛠️ Tech Stack

Python

Pandas

NumPy

Folium (for heatmap)

Random data synthesis (for demo use)



---

📘 How Judges Can View It

Open forecast_heatmap.html for visualization

Open forecast_report.txt for explanation

Use CSV files for data inspection


This engine is designed to help cities prepare for environmental risks before they happen.


---

🚀 Status

Branch 5 is completed and fully tested.
