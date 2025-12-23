# 🔋 Battery SOC Analysis

This is a small Python project where I analyzed survey data to understand
battery charging behavior and **State of Charge (SOC)** trends.

The goal of this project was to practice working with real-world data —
from loading and cleaning the dataset to generating insights using
visualizations.

---

## 📌 What this project is about

When users charge their devices, how much does the battery SOC actually
increase?  
Does charging time always result in better SOC gain?

To explore these questions, I worked with a survey-based dataset and used
Python to analyze and visualize the data.

This project helped me understand how data analysis works beyond just
writing code.

---

## 🛠 Tools I used

- **Python**
- **Pandas** – for reading, cleaning, and analyzing data
- **Matplotlib** – for creating graphs
- **CSV files** (Excel-compatible)

---

## 📂 Dataset details

The dataset contains basic information collected from a battery charging
survey:

| Column | Meaning |
|------|--------|
| User_ID | Unique ID for each user |
| Charging_Time_Hours | Time spent charging |
| SOC_Before | Battery SOC before charging (%) |
| SOC_After | Battery SOC after charging (%) |

Files included:
- `battery_survey.csv` → original dataset  
- `cleaned_battery_survey.csv` → cleaned and validated data  

---

## ⚙️ What I did step by step

1. Loaded the survey data using Pandas  
2. Checked the structure of the dataset and missing values  
3. Removed invalid SOC values (SOC must be between 0 and 100)  
4. Created a new column **SOC_Gain** to measure charging improvement  
5. Calculated basic statistics to understand trends  
6. Visualized SOC changes using graphs  

---

## 📊 Visual results

The analysis generates graphs that show:
- How much SOC increases after charging
- Patterns in charging behavior

These plots are saved as:
- `Figure_1.png`
- `Figure_2.png`

---

## 🚀 How to run this project

1. Make sure Python 3 is installed  
2. Install required libraries:

```bash
pip install pandas matplotlib


