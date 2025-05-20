# BSDA_Capstone
# 📊 Income Inequality Trends in the United States (2006–2023)

This capstone project analyzes trends in income inequality across U.S. states using Gini Index data from the American Community Survey (ACS) between 2006 and 2023. The goal is to assess whether income inequality has increased significantly across the majority of states and evaluate both the statistical and practical significance of those changes.

---

## 🧩 Research Question

**Has income inequality, as measured by the Gini Index, increased significantly across U.S. states since 2006?**

## 📁 Project Structure

Project root contains the following files and directories:

- `data_pull.py`  
  Pulls Gini Index and Median Household Income data from the U.S. Census API.

- `data_cleaning.py`  
  Processes raw data: cleans missing values, formats columns, adds regional labels.

- `eda_analysis.py`  
  Performs exploratory data analysis and generates visualizations.

- `statistical_test.py`  
  Conducts paired t-tests or Wilcoxon signed-rank tests; calculates Cohen's d.

- `data/`  
  - `raw/` — Unprocessed CSVs from Census API.  
  - `cleaned/` — Final cleaned dataset for analysis.

- `figures/`  
  Stores generated `.png` files, including:
  - `gini_histogram.png`  
  - `national_gini_trend.png`  
  - `regional_gini_trends.png`  
  - `gini_change_test_summary.png`  
  - `correlation_heatmap.png`  
  - `gini_vs_income_scatter.png`

- `results/`  
  Contains test result summaries, including p-values and test statistics.
 
- `README.md`  
  This documentation file.

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

Note: The year 2020 was intentionally excluded due to the U.S. Census Bureau not releasing ACS 1-Year Estimates that year because of COVID-19–related data disruptions. The year 2005 was also excluded because Gini Index values were not available in the 1-Year release for that period. These adjustments were handled by year-specific exception handling in `data_pull.py`.

---

## 📚 References

Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists, 50+ Essential Concepts Using R and Python* (2nd ed.). O'Reilly Media Inc.

Bureau, U. S. C. (2023, February 1, 2024). *Data Access and Use*. U.S. Census Bureau. Retrieved May 2, 2025, from https://www.census.gov/data/developers/about/terms-of-service.html

Cai, R., & Tan, S.-Y. (2025). Exploring the relationship between income inequality and crime in Toronto using frequentist and Bayesian models: Examining different crime types and spatial scales. *Environment and Planning B*, 0(0), 23998083241311969. https://doi.org/10.1177/23998083241311969

Grus, J. (2015). *Data Science from Scratch: First Principles with Python*. O'Reilly Media Inc.

Jackson, S. L. (2016). *Research Methods and Statistics: A Critical Thinking Approach*. Cengage Learning. https://books.google.com/books?id=M5CFCwAAQBAJ

Kuhn, M., Schularick, M., & Steins, U. I. (2017). Income and wealth inequality in America. *Journal of Political Economy*, 4.

McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with Pandas, NumPy & Jupyter*. O'Reilly Media Inc.

Molin, S. (2021). *Hands-On Data Analysis with Pandas*. Packt.

Rau, E. G., & Stokes, S. (2025). Income inequality and the erosion of democracy in the twenty-first century. *Proceedings of the National Academy of Sciences*, 122(1), e2422543121. https://doi.org/10.1073/pnas.2422543121

Scharrer, C. (2025). Evolving contributions of various income sources to US income inequality across age groups. *Journal of Population Ageing*. https://doi.org/10.1007/s12062-025-09481-0

Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. *Procedia Computer Science*, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199

Stotesbury, N., & Dorling, D. (2015). Understanding income inequality and its implications: Why better statistics are needed. *Statistics Views*, 21.

Tcherneva, P. (2015). Trends in US income inequality. *Real-World Economics Review*, 71, 64–74.

---

## ✅ Status

✔️ Completed  
📅 Timeline: May 10–May 19, 2025  
📂 Capstone Project Submission: BSDA Program

---

## 📬 Contact

**Author**: Mark MacPherson  
**Email**: mmacph6@wgo.edu  
**GitHub**: github.com/Scout7525