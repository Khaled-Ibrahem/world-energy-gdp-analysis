# World Energy & GDP Analysis

This project explores the relationships between **energy supply**, **renewable energy**, and **GDP** across countries. The data is cleaned, merged, and analyzed using Python and pandas, with insights derived from global datasets.

## 📁 Project Structure

- `assets/` — Folder containing the datasets:
  - `Energy Indicators.xls`
  - `scimagojr-3.xlsx`
  - `world_bank.csv`
- `analysis.py` — Contains the full code for data loading, cleaning, merging, and analysis.
- `README.md` — You’re reading it.

## 📊 Data Sources

1. **Energy Indicators**: Energy supply and % renewable from the UN.
2. **GDP**: GDP data from the World Bank (2006–2015).
3. **Scimago Journal Rank**: Country rankings by scientific output.

## ✅ Features Implemented

- Cleaned inconsistent country names and removed unnecessary columns/rows.
- Merged 3 datasets on country names.
- Computed statistics:
  - % renewable energy per country.
  - Estimated population.
  - Population aggregation by continent.
- Created binary indicators and binned data for grouped analysis.

## 📌 Key Tasks

- Create binary column based on median renewable energy.
- Group countries by continent using a dictionary.
- Calculate sample size, sum, mean, and standard deviation of estimated population.
- Bin % Renewable into 5 levels and group by continent.
- Format population estimates with thousands separators.

## 🛠️ Technologies Used

- Python 3
- pandas
- numpy
- Jupyter Notebook (optional)

## 🚀 Getting Started

Assignment 3 from Introduction to Data Science in Python course michigan university
