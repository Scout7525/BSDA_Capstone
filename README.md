# BSDA_Capstone
# 📊 Income Inequality Trends in the United States (2006–2023)

This capstone project analyzes trends in income inequality across U.S. states using Gini Index data from the American Community Survey (ACS) between 2006 and 2023. The goal is to assess whether income inequality has increased significantly across the majority of states and evaluate both the statistical and practical significance of those changes.

---

## 🧩 Research Question

**Has income inequality, as measured by the Gini Index, increased significantly across U.S. states since 2006?**

---

## 📁 Project Structure

├── data_pull.py # Script to pull Gini Index data via Census API
├── data_cleaning.py # Cleans and prepares raw ACS data
├── eda_analysis.py # Generates plots and summary statistics
├── statistical_test.py # Performs paired t-test, Wilcoxon, effect size
├── data/
│ ├── raw/ # Original pulled data (CSV)
│ └── cleaned/ # Processed data for analysis
├── figures/
│ ├── gini_change_test_summary.png
│ ├── correlation_heatmap.png
│ ├── regional_gini_trends.png
│ └── ...
├── results/
│ └── hypothesis_test_summary.txt # Output test results and stats
├── README.md # Project documentation (this file)
---

## 🛠️ Tools & Libraries

- **Python 3.11**
- `pandas` – data manipulation
- `requests` – API data fetching
- `matplotlib` & `seaborn` – visualization
- `scipy.stats` – statistical testing
- `os`, `datetime` – automation and file handling

---

## 📊 Analytical Methods

- **Descriptive Analysis**:
  - Time series plots of Gini Index by region and state
  - Correlation heatmaps and histograms of distribution
- **Diagnostic Analysis**:
  - Normality test (Shapiro-Wilk)
  - Paired t-test or Wilcoxon signed-rank test
  - Cohen’s d for effect size
- **Visualization**:
  - Annotated figures summarizing statistical output
  - Regional and state-level Gini Index trends

---

## 📌 Key Findings

- A **statistically significant** increase in the Gini Index was observed across most U.S. states (p < 0.0001).
- **Cohen's d = 1.65**, indicating a large practical effect.
- The **South and West** regions saw the most consistent growth in inequality.
- **Weak correlation** (r ≈ 0.14) between Gini Index and median household income, indicating that higher income does not imply lower inequality.

---

## 📁 Sample Visual Outputs

- 📈 `national_gini_trend.png` – U.S. average Gini over time  
- 🌎 `regional_gini_trends.png` – Gini by Census region  
- 🧪 `gini_change_test_summary.png` – Hypothesis test and result visualization  
- 🧮 `correlation_heatmap.png` – Correlation of Gini, income, year

---

## 📄 Data Source

Data is sourced from the **U.S. Census Bureau's American Community Survey (ACS) 1-Year Estimates**, using public APIs:  
🔗 https://www.census.gov/data/developers/data-sets/acs-1year.html

---

## 📑 References

- Scharrer, C. (2025). *Evolving Contributions of Various Income Sources to U.S. Income Inequality*.
- Kuhn, M., Schularick, M., & Steins, U. (2017). *Income and Wealth Inequality in America, 1949–2013*.
- Rau, E. G., & Stokes, S. (2025). *Income Inequality and the Erosion of Democracy*.
- U.S. Census Bureau (n.d.). *American Community Survey API*.

---

## ✅ Status

✔️ Completed  
📅 Timeline: May 10–May 18, 2025  
📂 Capstone Project Submission: BSDA Program

---

## 📬 Contact

**Author**: Mark MacPherson]  
**Email**: mmacph6@wgo.edu]  
**GitHub**: github.com/Scout7525

