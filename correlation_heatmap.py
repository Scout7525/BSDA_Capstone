import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
input_file = "./data/income_inequality_cleaned.csv"
df = pd.read_csv(input_file)

# Create figures directory if not exists
os.makedirs("./figures", exist_ok=True)

# Filter to numeric columns only
numeric_df = df.select_dtypes(include=["float64", "int64"])

# Compute correlation matrix
corr = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title("Correlation Heatmap of Income Inequality Data")
plt.tight_layout()

# Save the heatmap to a file
output_file = "./figures/correlation_heatmap.png"
plt.savefig(output_file)
plt.close()

print(f"✅ Correlation heatmap saved to: {output_file}")
