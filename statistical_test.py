import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load cleaned data
input_file = "./data/income_inequality_cleaned.csv"
df = pd.read_csv(input_file)

# Identify first and last year available
start_year = df["Year"].min()
end_year = df["Year"].max()

print(f"📅 Running comparison between {start_year} and {end_year}")

# Filter to only states that exist in both years
start_df = df[df["Year"] == start_year].set_index("State")[["Gini_Index"]]
end_df = df[df["Year"] == end_year].set_index("State")[["Gini_Index"]]

# Merge to get paired values
paired = start_df.join(end_df, lsuffix="_start", rsuffix="_end", how="inner").dropna()
paired["Gini_Change"] = paired["Gini_Index_end"] - paired["Gini_Index_start"]

# Run Shapiro-Wilk normality test
shapiro_stat, shapiro_p = stats.shapiro(paired["Gini_Change"])

# Choose appropriate test
if shapiro_p > 0.05:
    test_name = "Paired t-test"
    t_stat, p_val = stats.ttest_rel(
        paired["Gini_Index_end"],
        paired["Gini_Index_start"],
        alternative="greater"
    )
else:
    test_name = "Wilcoxon Signed-Rank Test"
    t_stat, p_val = stats.wilcoxon(
        paired["Gini_Index_end"],
        paired["Gini_Index_start"],
        alternative="greater"
    )

# Effect size (Cohen's d)
mean_diff = paired["Gini_Change"].mean()
std_diff = paired["Gini_Change"].std()
cohens_d = mean_diff / std_diff

# Interpretation
alpha = 0.05
if p_val < alpha:
    result = "✅ Reject null hypothesis. Income inequality has significantly increased."
else:
    result = "❌ Fail to reject null. No statistically significant increase detected."

# --------- Plotting and Saving Summary ---------
plt.figure(figsize=(10, 6))
sns.histplot(paired["Gini_Change"], kde=True, color='skyblue')
plt.title("Change in Gini Index Distribution & Test Results")
plt.axvline(0, color='black', linestyle='--')

# Annotated result box
text_str = (
    f"Normality Test (Shapiro-Wilk): p = {shapiro_p:.4f}\n"
    f"Test Used: {test_name}\n"
    f"Test Statistic: {t_stat:.4f}\n"
    f"P-Value: {p_val:.4f}\n"
    f"Cohen's d: {cohens_d:.4f}\n"
    f"Conclusion:\n{result}"
)

plt.gcf().text(0.05, 0.4, text_str, fontsize=10, bbox=dict(facecolor='white', alpha=0.9))
plt.tight_layout()

# Save figure
output_path = "./figures/gini_change_test_summary.png"
plt.savefig(output_path)
plt.close()

print(f"✅ Analysis complete. Summary saved to: {output_path}")

