import os
import requests
import pandas as pd
from time import sleep

# ---------------------- CONFIGURATION -----------------------
CENSUS_API_KEY = "caa8b48ff6f8c9182650f3b765073d0facf90bbb"  
BASE_URL = "https://api.census.gov/data/{year}/acs/acs1"
YEARS = list(range(2005, 2024))  # 2005 through 2023

# Variables to pull: Gini Index and Median Household Income
VARIABLES = {
    "Gini_Index": "B19083_001E",
    "Median_Household_Income": "B19013_001E"
}

OUTPUT_DIR = "./data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mapping of FIPS codes to readable state names
STATE_FIPS_TO_NAME = {
    "01": "Alabama", "02": "Alaska", "04": "Arizona", "05": "Arkansas", "06": "California",
    "08": "Colorado", "09": "Connecticut", "10": "Delaware", "11": "District of Columbia",
    "12": "Florida", "13": "Georgia", "15": "Hawaii", "16": "Idaho", "17": "Illinois",
    "18": "Indiana", "19": "Iowa", "20": "Kansas", "21": "Kentucky", "22": "Louisiana",
    "23": "Maine", "24": "Maryland", "25": "Massachusetts", "26": "Michigan",
    "27": "Minnesota", "28": "Mississippi", "29": "Missouri", "30": "Montana",
    "31": "Nebraska", "32": "Nevada", "33": "New Hampshire", "34": "New Jersey",
    "35": "New Mexico", "36": "New York", "37": "North Carolina", "38": "North Dakota",
    "39": "Ohio", "40": "Oklahoma", "41": "Oregon", "42": "Pennsylvania",
    "44": "Rhode Island", "45": "South Carolina", "46": "South Dakota", "47": "Tennessee",
    "48": "Texas", "49": "Utah", "50": "Vermont", "51": "Virginia", "53": "Washington",
    "54": "West Virginia", "55": "Wisconsin", "56": "Wyoming"
}
# -------------------------------------------------------------

def pull_acs_data(year):
    """Gracefully pulls ACS data for a specific year and returns a clean DataFrame."""
    url = BASE_URL.format(year=year)
    params = {
        "get": ",".join(VARIABLES.values()),
        "for": "state:*",
        "key": CENSUS_API_KEY
    }

    print(f"✨ Pulling data for {year}...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"😢 Failed to fetch data for {year}: {response.text}")

    # Parse and beautify
    data = response.json()
    columns = list(VARIABLES.keys()) + ["state"]
    df = pd.DataFrame(data[1:], columns=columns)
    df["Year"] = year
    df["State"] = df["state"].map(STATE_FIPS_TO_NAME)
    df.drop(columns=["state"], inplace=True)

    # Ensure numeric values are correctly typed
    for col in VARIABLES.keys():
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def main():
    all_years_data = []

    for year in YEARS:
        try:
            df = pull_acs_data(year)
            all_years_data.append(df)
            sleep(1)  
        except Exception as e:
            print(f"⚠️ Error encountered for year {year}: {e}")

    full_df = pd.concat(all_years_data, ignore_index=True)
    output_file = os.path.join(OUTPUT_DIR, "income_inequality_trends.csv")
    full_df.to_csv(output_file, index=False)
    print(f"\n✅ Successfully saved data to: {output_file}")

if __name__ == "__main__":
    main()
