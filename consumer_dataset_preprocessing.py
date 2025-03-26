import pandas as pd
from datetime import datetime

print("Your dataset is under preprocessing phase...")

def calculate_days(start_date, end_date):
    if pd.isna(start_date) or pd.isna(end_date):
        return "N/A"
    
    if isinstance(start_date, str):
        start_date = start_date.strip().lower()
    if isinstance(end_date, str):
        end_date = end_date.strip().lower()
    
    if start_date in ["declined", "pending"] or end_date in ["declined", "pending"]:
        return "Pending" if "pending" in [start_date, end_date] else "N/A"
    
    try:
        start_dt = pd.to_datetime(start_date, format="%d-%m-%Y", errors='coerce')
        end_dt = pd.to_datetime(end_date, format="%d-%m-%Y", errors='coerce')
        if pd.isna(start_dt) or pd.isna(end_dt):
            return "N/A"
        
        # Calculate days INCLUDING both start and end dates
        days = (end_dt - start_dt).days + 1  # Key change here (+1)
        return days
    except Exception as e:
        print(f"Error calculating days: {e}")
        return "N/A"

def preprocess_data(input_file, output_file):
    
    df = pd.read_csv(input_file, dtype=str)
    
    # Replace applymap with map for element-wise operation
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    
    date_columns = [
        "Registration Date", "Application Approved Date", "Vendor Selection Date",
        "Vendor Acceptance Date", "Installation Date", "Inspection Date",
        "Subsidy Redeemed Date", "Subsidy Released Date"
    ]
    
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format="%d-%m-%Y", errors='coerce')
    
    accepted_mask = df["Acceptance Status"].str.lower() == "accepted"
    
    date_pairs = [
        ("Registration Date", "Application Approved Date", "Registration to Approval Days"),
        ("Application Approved Date", "Vendor Selection Date", "Approval to Vendor Selection Days"),
        ("Vendor Selection Date", "Vendor Acceptance Date", "Vendor Selection to Acceptance Days"),
        ("Vendor Acceptance Date", "Installation Date", "Acceptance to Installation Days"),
        ("Installation Date", "Inspection Date", "Installation to Inspection Days"),
        ("Inspection Date", "Subsidy Redeemed Date", "Inspection to Subsidy Redeemed Days"),
        ("Subsidy Redeemed Date", "Subsidy Released Date", "Subsidy Redeemed to Released Days")
    ]
    
    for start_col, end_col, new_col in date_pairs:
        df.loc[accepted_mask, new_col] = df.loc[accepted_mask].apply(
            lambda row: calculate_days(row[start_col], row[end_col]), axis=1
        )
    
    rejected_mask = df["Acceptance Status"].str.lower() == "rejected"
    new_columns = [col[2] for col in date_pairs]
    df.loc[rejected_mask, new_columns] = "N/A"
    
    # Replace empty cells with 'NULL'
    df.fillna("NULL", inplace=True)

    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

# File paths
input_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# Run preprocessing
preprocess_data(input_file, output_file)
