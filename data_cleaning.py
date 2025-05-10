import pandas as pd
import os

# Load raw data
input_file = "./data/income_inequality_trends.csv"
output_file = "./data/income_inequality_cleaned.csv"

df = pd.read_csv(input_file)

# Drop rows with missing state
df = df.dropna(subset=["State"])

# Strip whitespace from state names (just in case)
df["State"] = df["State"].str.strip()

# Define regions for optional grouped analysis
region_map = {
    "Northeast": ["Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island", "Vermont", "New Jersey", "New York", "Pennsylvania"],
    "Midwest": ["Illinois", "Indiana", "Iowa", "Kansas", "Michigan", "Minnesota", "Missouri", "Nebraska", "North Dakota", "Ohio", "South Dakota", "Wisconsin"],
    "South": ["Alabama", "Arkansas", "Delaware", "Florida", "Georgia", "Kentucky", "Louisiana", "Maryland", "Mississippi", "North Carolina", "Oklahoma", "South Carolina", "Tennessee", "Texas", "Virginia", "West Virginia", "District of Columbia"],
    "West": ["Alaska", "Arizona", "California", "Colorado", "Hawaii", "Idaho", "Montana", "Nevada", "New Mexico", "Oregon", "Utah", "Washington", "Wyoming"]
}

# Assign region to each row
def assign_region(state):
    for region, states in region_map.items():
        if state in states:
            return region
    return "Unknown"

df["Region"] = df["State"].apply(assign_region)

# Ensure numeric types
df["Gini_Index"] = pd.to_numeric(df["Gini_Index"], errors="coerce")
df["Median_Household_Income"] = pd.to_numeric(df["Median_Household_Income"], errors="coerce")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Save cleaned version
df.to_csv(output_file, index=False)
print(f"✅ Cleaned dataset saved to: {output_file}")
