import pandas as pd

# Define file locations
input_file = r"D:\Projects\RTS Analysis\consumer_application_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.xlsx"

# List of columns to extract
columns_to_extract = [
    "Application Number", "Gender", "State/UT", "District", "Discom Name",
    "Registration Date", "Acceptance Status", "Production Capacity (KW)",
    "Application Approved Date", "Vendor Organization", "Vendor Selection Date",
    "Vendor Acceptance Date", "Installation Date", "Inspection Date",
    "Subsidy Redeemed Date", "Subsidy Released Date"
]

# Read CSV file and extract required columns
df = pd.read_csv(input_file, usecols=columns_to_extract)

# Save extracted data to a new Excel file
df.to_excel(output_file, index=False)
print(f"Preprocessed data saved to: {output_file}")
