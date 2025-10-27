# 🧑‍🌾 FarmGate Dashboard

This project presents a fully interactive dashboard for visualizing agricultural commodity data at the farmgate level. The data was extracted from the [JAMIS (Jamaica Agricultural Market Information System)](https://jamis.gov.jm) website using Python, processed for analysis, and rendered in an intuitive web-based interface.

## 📊 Project Overview

The **FarmGate Dashboard** provides insights into:
- Weekly and monthly price trends of major agricultural commodities
- Regional comparisons of farmgate prices
- Seasonal price fluctuations
- Data filtering by parish, commodity type, and time range

This tool is intended to support farmers, policymakers, researchers, and agribusiness professionals in making data-driven decisions.

## 🛠️ Features

- 🐍 **Automated Web Scraping**: Extracts and updates data from JAMIS using Python and BeautifulSoup
- 📈 **Dynamic Visualizations**: Interactive charts and graphs powered by Plotly/Dash or Streamlit
- 🧹 **Data Cleaning Pipeline**: Handles formatting inconsistencies and missing values
- 🌎 **Geographic Filters**: Analyze commodity prices across different parishes
- ⏱ **Time-Series Analysis**: Observe trends over custom time windows

## 🗂️ Tech Stack

- **Python** (Pandas, BeautifulSoup, Requests)
- **Streamlit** or **Dash** for the dashboard interface
- **Plotly** / **Altair** for data visualization
- **GitHub Actions** *(optional)*: for automated scraping and dashboard updates

## 📁 Project Structure
farmgate-dashboard/
│
├── data/ # Cleaned datasets for dashboard use
├── notebooks/ # Data extraction and exploration notebooks
├── src/ # Python scripts for scraping and preprocessing
│ ├── scraper.py
│ └── clean_data.py
├── dashboard/ # Dashboard implementation (Streamlit or Dash)
│ └── home.py
├── requirements.txt
└── README.md


