import pandas as pd
from ydata_profiling import ProfileReport

# Define file location
file_path = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

# Generate report
profile = ProfileReport(df, title="Solar Data Analysis", explorative=True)

# Save report as HTML
profile.to_file("solar_analysis_report.html")

print("Report saved as solar_analysis_report.html")
