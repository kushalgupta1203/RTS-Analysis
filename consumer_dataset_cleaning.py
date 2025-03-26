import pandas as pd

print(f"Your dataset is in under cleaning phase...")

# Define file locations
input_file = r"D:\Projects\RTS Analysis\consumer_application_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"

# List of columns to extract
columns_to_extract = [
    "Application Number", "Gender", "State/UT", "District", "RWA/Residential", "Discom Name",
    "Acceptance Status", "Production Capacity (KW)",  "Vendor Organization",
    "Registration Date", "Application Approved Date", "Vendor Selection Date",
    "Vendor Acceptance Date", "Installation Date", "Inspection Date",
    "Subsidy Redeemed Date", "Subsidy Released Date"
]

# Read CSV file and extract required columns
df = pd.read_csv(input_file, usecols=columns_to_extract)

# Save extracted data to a new Excel file
df.to_csv(output_file, index=False)
print(f"Data cleaning complete. CSV file created: consumer_cleaned_data.csv")