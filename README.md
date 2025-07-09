# 🌤️ Simple weather analysis — Multi-City Insights for Climate Trends & Decision Support

## 📍 Overview

This project explores a fictional weather dataset containing multi-city records of temperature, humidity, precipitation, wind speed, and timestamps. The goal is to simulate a real-world data analysis scenario that supports insights for planning, risk management, and operational decisions.

Designed as a portfolio project, it highlights core data analysis skills including exploratory data analysis (EDA), temporal trend evaluation, geographic comparisons, anomaly detection, and stakeholder-style reporting.

---

## 🎯 Objectives

- Summarize weather patterns by city and season to support high-level operational planning.
- Identify time periods or cities with extreme or volatile weather conditions.
- Detect long-term or seasonal climate shifts using time-series techniques.
- Explore relationships between temperature, humidity, precipitation, and wind speed.
- Communicate findings visually and narratively for a general (non-technical) audience.

---

## ❓ Key Business Questions

- Which cities experience the most stable or volatile weather conditions throughout the year?
- What are the seasonal patterns in temperature, humidity, and precipitation across different cities?
- Are there strong correlations between humidity and temperature, or wind speed and precipitation?
- What are the most extreme weather events (e.g., heatwaves, high winds), and how often do they occur?
- How does weather vary within a typical day across different cities?

---

## 📊 Dataset Description

**Columns:**
- `location` – Name of the city
- `datetime` – Timestamp of observation
- `temperature` – Recorded temperature (°C)
- `humidity` – Humidity as a percentage
- `precipitation` – Precipitation level (mm)
- `wind_speed` – Wind speed (km/h)

> ⚠️ **Note:** This is a synthetic dataset designed for skill demonstration only.

---

## 🛠️ Tools & Technologies

- **Python:** pandas, NumPy, matplotlib, seaborn
- **Jupyter Notebook:** for iterative analysis and storytelling
- **Skills Demonstrated:** data cleaning, EDA, time series analysis, trend detection, data visualization, business question framing

---

## 📁 Project Structure

```
.
├── 📁code
│   ├── 📁utilities
│   │   ├── __init__.py
│   │   └── config.py
│   └── notebook.ipynb
├── 📁data
│   ├── duplicates.csv
│   ├── processed_weather.csv
│   └── raw_weather.csv
├── 📁products
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md
```
