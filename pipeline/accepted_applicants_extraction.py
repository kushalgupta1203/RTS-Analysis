import pandas as pd
import numpy as np

print("Your data is getting transformed...")

# Define the input and output file paths
input_file_path = r"D:\Projects\RTS Analysis\dataset\consumer_preprocessed_data.csv"
output_file_path = r"D:\Projects\RTS Analysis\dataset\accepted_applicants.csv"

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(input_file_path)
except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
    exit()
except pd.errors.EmptyDataError:
    print(f"Error: The file {input_file_path} is empty.")
    exit()

# Check if the column exists in the DataFrame
if 'Acceptance Status' not in df.columns:
    print("Error: Column 'Acceptance Status' does not exist in the input file.")
    exit()

# Replace "Pending", "N/A", or blank spaces with an empty string across all columns
df.replace(to_replace=["Pending", "N/A", r'^\s*$'], value="", regex=True, inplace=True)

# Filter the DataFrame for rows where acceptance status is 'Accepted'
accepted_df = df[df['Acceptance Status'].str.lower() == 'accepted']

# Check if any rows were filtered
if accepted_df.empty:
    print("No rows found with 'Acceptance Status' as 'Accepted'.")
else:
    # Write the filtered DataFrame to a new CSV file
    accepted_df.to_csv(output_file_path, index=False)
    print(f"Transformed data has been written to {output_file_path}.")
