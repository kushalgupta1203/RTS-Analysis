import pandas as pd

# Define the file location and columns to extract
input_file = r"D:\Projects\RTS Analysis\consumer_application_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# List of columns to be extracted
columns_to_extract = [
    "application_number",
    "gender",
    "state_ut",
    "district",
    "discom_name",
    "registration_date",
    "application_approved_date",
    "vendor_organization",
    "vendor_selection_date",
    "vendor_acceptance_date",
    "installation_date",
    "inspection_date",
    "claim_submission_date",
    "claim_release_date"
]

# Read the CSV file
try:
    df = pd.read_csv(input_file, usecols=columns_to_extract)
    
    # Rename columns to remove underscores and capitalize first letter
    df.columns = [col.replace('_', ' ').title() for col in df.columns]
    
    # Ensure 'Application Number' is the first column
    reordered_columns = ['Application Number'] + [col for col in df.columns if col != 'Application Number']
    df = df[reordered_columns]
    
    # Write the new DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Data extracted successfully to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
