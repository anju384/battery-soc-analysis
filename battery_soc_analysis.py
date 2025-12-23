# Survey Data Analysis for Battery SOC
# Tools: Python, Pandas, Matplotlib, Excel (optional)

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: LOAD DATA
# -----------------------------
df = pd.read_csv("battery_survey.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

# -----------------------------
# STEP 2: DATA CLEANING
# -----------------------------
print("\nChecking missing values:")
print(df.isnull().sum())

# Remove invalid SOC values
df = df[(df["SOC_Before"] >= 0) & (df["SOC_After"] <= 100)]

# -----------------------------
# STEP 3: FEATURE CREATION
# -----------------------------
df["SOC_Gain"] = df["SOC_After"] - df["SOC_Before"]

print("\nSOC Gain calculated:")
print(df[["SOC_Before", "SOC_After", "SOC_Gain"]])

# -----------------------------
# STEP 4: BASIC ANALYSIS
# -----------------------------
avg_gain = df["SOC_Gain"].mean()
print("\nAverage SOC Gain:", avg_gain)

charger_analysis = df.groupby("Charger_Type")["SOC_Gain"].mean()
print("\nAverage SOC Gain by Charger Type:")
print(charger_analysis)

# -----------------------------
# STEP 5: VISUALIZATION
# -----------------------------
plt.figure()
plt.hist(df["SOC_Gain"], bins=5)
plt.xlabel("SOC Gain")
plt.ylabel("Frequency")
plt.title("Distribution of SOC Gain")
plt.show()

plt.figure()
charger_analysis.plot(kind="bar")
plt.xlabel("Charger Type")
plt.ylabel("Average SOC Gain")
plt.title("SOC Gain by Charger Type")
plt.show()

# -----------------------------
# STEP 6: SAVE CLEANED DATA
# -----------------------------
df.to_csv("cleaned_battery_survey.csv", index=False)
print("\nCleaned data saved as cleaned_battery_survey.csv")
