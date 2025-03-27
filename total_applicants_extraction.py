import pandas as pd
import numpy as np

print("Your data is getting transformed...")

# Define the input and output file paths
input_file_path = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"
output_file_path = r"D:\Projects\RTS Analysis\total_applicants_data.csv"

# Read the input CSV file
data = pd.read_csv(input_file_path)

# Replace specified values with blank
data.replace({"NULL": "", "N/A": "", "Pending": "","Declined": ""}, inplace=True)

# Save the transformed data to a new CSV file
data.to_csv(output_file_path, index=False)

print("Data transformation complete. The transformed data is saved at:", output_file_path)
