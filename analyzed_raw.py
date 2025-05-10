import pandas as pd

# Load the uploaded CSV
file_path = "/home/scout/BSDA_Capstone/data/income_inequality_trends.csv"
df = pd.read_csv(file_path)

# Show basic info 
df.info()
