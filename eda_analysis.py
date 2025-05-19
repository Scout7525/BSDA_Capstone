import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Setup
sns.set(style="whitegrid")
input_file = "./data/income_inequality_cleaned.csv"
output_dir = "./figures"
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_file)

# --------- BASIC EDA ---------

# Overview
print("\n🔍 Dataset Overview:")
print(df.info())
print(df.describe())

# Check for missing
print("\n🧼 Missing Values:\n", df.isnull().sum())

# --------- NATIONAL GINI TREND ---------

national_trend = df.groupby("Year")["Gini_Index"].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=national_trend, x="Year", y="Gini_Index", marker="o")
plt.title("National Average Gini Index Over Time")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.ticker import MaxNLocator

# Setup
sns.set(style="whitegrid")
input_file = "./data/income_inequality_cleaned.csv"
output_dir = "./figures"
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_file)

# --------- BASIC EDA ---------

print("\n🔍 Dataset Overview:")
print(df.info())
print(df.describe())

print("\n🧼 Missing Values:\n", df.isnull().sum())

# --------- NATIONAL GINI TREND ---------

national_trend = df.groupby("Year")["Gini_Index"].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=national_trend, x="Year", y="Gini_Index", marker="o")
plt.title("National Average Gini Index Over Time")
plt.ylabel("Gini Index")
plt.xlabel("Year")
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(f"{output_dir}/national_gini_trend.png")
plt.close()

# --------- REGIONAL GINI TRENDS ---------

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Year", y="Gini_Index", hue="Region", ci=None)
plt.title("Regional Gini Index Trends (2006–2023)")
plt.ylabel("Gini Index")
plt.xlabel("Year")
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.legend(title="Region")
plt.tight_layout()
plt.savefig(f"{output_dir}/regional_gini_trends.png")
plt.close()

# --------- HISTOGRAM: GINI INDEX ---------

plt.figure(figsize=(8, 5))
sns.histplot(df["Gini_Index"], bins=20, kde=True)
plt.title("Distribution of Gini Index Values")
plt.xlabel("Gini Index")
plt.tight_layout()
plt.savefig(f"{output_dir}/gini_histogram.png")
plt.close()

# --------- CORRELATION: GINI vs INCOME ---------

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Median_Household_Income", y="Gini_Index", hue="Region")
plt.title("Gini Index vs Median Household Income")
plt.tight_layout()
plt.savefig(f"{output_dir}/gini_vs_income_scatter.png")
plt.close()

correlation = df[["Gini_Index", "Median_Household_Income"]].corr().iloc[0, 1]
print(f"\n📈 Correlation between Gini Index and Median Income: {correlation:.4f}")

# --------- STATE-LEVEL TREND EXAMPLE ---------

sample_states = ["California", "Texas", "New York", "Florida"]
plt.figure(figsize=(12, 6))
sns.lineplot(data=df[df["State"].isin(sample_states)], x="Year", y="Gini_Index", hue="State", marker="o")
plt.title("Gini Index Trends in Selected States")
plt.ylabel("Gini Index")
plt.xlabel("Year")
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(f"{output_dir}/selected_states_gini_trends.png")
plt.close()

print(f"\n✅ All EDA plots saved to: {output_dir}")
