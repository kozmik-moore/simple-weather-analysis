# Simple weather analysis — Multi-City Insights for Climate Trends & Decision Support

## Overview

This project explores a fictional weather dataset containing multi-city records of temperature, humidity, precipitation, wind speed, and timestamps. The goal is to simulate a real-world data analysis scenario that supports insights for planning, risk management, and operational decisions.

Designed as a portfolio project, it highlights core data analysis skills including exploratory data analysis (EDA), temporal trend evaluation, geographic comparisons, anomaly detection, and stakeholder-style reporting. The notebook can be viewed directly [here](/code/notebook.ipynb).

---

## Objectives

- Summarize weather patterns by city and season to support high-level operational planning.
- Identify time periods or cities with extreme or volatile weather conditions.
- Detect long-term or seasonal climate shifts using time-series techniques.
- Explore relationships between temperature, humidity, precipitation, and wind speed.
- Communicate findings visually and narratively for a general (non-technical) audience.

---

## Key Business Questions

- Which cities experience the most stable or volatile weather conditions throughout the year?
- What are the seasonal patterns in temperature, humidity, and precipitation across different cities?
- Are there strong correlations between humidity and temperature, or wind speed and precipitation?
- What are the most extreme weather events (e.g., heatwaves, high winds), and how often do they occur?
- How does weather vary within a typical day across different cities?

---

## Dataset Description

**Columns:**
- `location` – Name of the city
- `datetime` – Timestamp of observation
- `temperature` – Recorded temperature (°C)
- `humidity` – Humidity as a percentage
- `precipitation` – Precipitation level (mm)
- `wind_speed` – Wind speed (km/h)

> ⚠️ **Note:** This is a synthetic dataset designed for skill demonstration only.

---

## Tools & Technologies

- **Python:** pandas, NumPy, matplotlib, seaborn
- **Jupyter Notebook:** for iterative analysis and storytelling
- **Skills Demonstrated:** data cleaning, EDA, time series analysis, trend detection, data visualization, business question framing

---

## Project Structure

```
└── 📁simple-weather-analysis
    └── 📁assets
    └── 📁code
        └── 📁utilities
            ├── __init__.py
            ├── config.py
        ├── notebook.ipynb
    └── 📁data
        ├── duplicates.csv
        ├── processed_weather.csv
        ├── raw_weather.csv
    └── 📁products
        └── 📁images
            └── 📁averages
                └── 📁cumulative
                    ├── Daily cumulative averages for Chicago.png
                    ├── Daily cumulative averages for Dallas.png
                    ├── Daily cumulative averages for Houston.png
                    ├── Daily cumulative averages for Los Angeles.png
                    ├── Daily cumulative averages for New York.png
                    ├── Daily cumulative averages for Philadelphia.png
                    ├── Daily cumulative averages for Phoenix.png
                    ├── Daily cumulative averages for San Antonio.png
                    ├── Daily cumulative averages for San Diego.png
                    ├── Daily cumulative averages for San Jose.png
                └── 📁daily
                    ├── Daily average for humidity by location.png
                    ├── Daily average for precipitation by location.png
                    ├── Daily average for temperature by location.png
                    ├── Daily average for windspeed by location.png
                └── 📁monthly
                    ├── Monthly average for humidity by location.png
                    ├── Monthly average for precipitation by location (without Phoenix).png
                    ├── Monthly average for precipitation by location.png
                    ├── Monthly average for temperature by location (without Phoenix).png
                    ├── Monthly average for temperature by location.png
                    ├── Monthly average for windspeed by location.png
                └── 📁rolling
                    ├── Daily rolling averages for Chicago.png
                    ├── Daily rolling averages for Dallas.png
                    ├── Daily rolling averages for Houston.png
                    ├── Daily rolling averages for Los Angeles.png
                    ├── Daily rolling averages for New York.png
                    ├── Daily rolling averages for Philadelphia.png
                    ├── Daily rolling averages for Phoenix.png
                    ├── Daily rolling averages for San Antonio.png
                    ├── Daily rolling averages for San Diego.png
                    ├── Daily rolling averages for San Jose.png
                └── 📁time of day
                    ├── Average humidity by time of day and location.png
                    ├── Average precipitation by time of day and location (without Phoenix).png
                    ├── Average precipitation by time of day and location.png
                    ├── Average temperature by time of day and location (without Phoenix).png
                    ├── Average temperature by time of day and location.png
                    ├── Average windspeed by time of day and location.png
                ├── Numeric averages by location.png
            └── 📁distributions
                ├── humidity_distribution.png
                ├── numeric_distibutions_boxplot.png
                ├── precipitation_distribution.png
                ├── temperature_distribution.png
                ├── windspeed_distribution.png
            ├── Numeric correlations.png
    ├── .gitattributes
    ├── .gitignore
    ├── LICENSE
    └── README.md
```