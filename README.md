# 🔋 Battery SOC Analysis

Survey Data Analysis for Battery **State of Charge (SOC)** using Python.

---

## 📌 Project Overview

This project analyzes survey-based battery charging data to understand
charging behavior and State of Charge (SOC) trends.  
It demonstrates real-world data analysis steps including data cleaning,
feature engineering, and visualization.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas** – data manipulation and analysis
- **Matplotlib** – data visualization
- **CSV / Excel-compatible datasets**

---

## 📂 Dataset Description

The survey dataset contains the following fields:

| Column Name | Description |
|------------|------------|
| User_ID | Unique user identifier |
| Charging_Time_Hours | Time spent charging |
| SOC_Before | Battery SOC before charging (%) |
| SOC_After | Battery SOC after charging (%) |

Two datasets are used:
- `battery_survey.csv` – raw survey data
- `cleaned_battery_survey.csv` – cleaned and validated data

---

## ⚙️ Project Workflow

1. Load survey data using Pandas  
2. Inspect dataset structure and missing values  
3. Clean invalid SOC values (range 0–100)  
4. Create a new feature **SOC_Gain**  
5. Perform basic statistical analysis  
6. Visualize SOC changes using graphs  

---

## 📊 Visualizations

The project generates plots to analyze:
- SOC gain after charging
- Charging behavior patterns

Example outputs:
- `Figure_1.png`
- `Figure_2.png`

---

## 🚀 How to Run the Project

1. Clone the repository or download the files
2. Ensure Python 3 is installed
3. Install required libraries:

```bash
pip install pandas matplotlib
