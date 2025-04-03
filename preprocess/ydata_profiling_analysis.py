import pandas as pd
from ydata_profiling import ProfileReport

# Define file location
file_path = r"D:\Projects\RTS Analysis\dataset\consumer_preprocessed_data.csv"

# Read Excel file
df = pd.read_csv(file_path)

# Generate report
profile = ProfileReport(df, title="Solar Data Analysis", explorative=True)

# Save report as HTML
profile.to_file("testing.html")

print("Report saved as testing.html")
