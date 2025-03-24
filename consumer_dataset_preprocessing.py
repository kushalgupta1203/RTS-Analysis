import pandas as pd
from ydata_profiling import ProfileReport  

# Define the file location and columns to extract
input_file = r"D:\Projects\RTS Analysis\consumer_application_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# List of columns to be extracted (Fixed Commas & List Syntax)
columns_to_extract = [
    "Application Number",
    "Gender",
    "State/UT",
    "District",
    "Discom Name",
    "Registration Date",
    "Acceptance Status",
    "Production Capacity (KW)",
    "Application Approved Date",
    "Vendor Organization",
    "Vendor Selection Date",
    "Vendor Acceptance Date",
    "Installation Date",
    "Inspection Date",
    "Subsidy Redeemed Date",
    "Subsidy Released Date"
]

# Read the CSV file (Fixed Path)
df = pd.read_csv(input_file, usecols=columns_to_extract)

# Generate the profiling report
profile = ProfileReport(df, title="Solar Energy Applicants Report", explorative=True)

# Save the report to an HTML file
profile.to_file("solar_applicant_sample_report.html")

# To view directly in Jupyter Notebook
profile.to_notebook_iframe()
