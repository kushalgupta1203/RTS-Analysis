import pandas as pd
from datetime import datetime

def calculate_days(start_date, end_date):
    if start_date in ["declined", "pending"] or end_date in ["declined", "pending"]:
        return "N/A" if start_date == "declined" or end_date == "declined" else "pending"
    try:
        start_dt = datetime.strptime(start_date, "%d-%m-%Y")
        end_dt = datetime.strptime(end_date, "%d-%m-%Y")
        return (end_dt - start_dt).days
    except ValueError:
        return "N/A"

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Define the date columns for processing
    date_columns = [
        "Registration Date", "Application Approved Date", "Vendor Selection Date",
        "Vendor Acceptance Date", "Installation Date", "Inspection Date",
        "Subsidy Redeemed Date", "Subsidy Released Date"
    ]
    
    # Creating new columns for phase durations
    df["Registration to Approval Days"] = df.apply(lambda row: calculate_days(row["Registration Date"], row["Application Approved Date"]), axis=1)
    df["Approval to Vendor Selection Days"] = df.apply(lambda row: calculate_days(row["Application Approved Date"], row["Vendor Selection Date"]), axis=1)
    df["Vendor Selection to Acceptance Days"] = df.apply(lambda row: calculate_days(row["Vendor Selection Date"], row["Vendor Acceptance Date"]), axis=1)
    df["Acceptance to Installation Days"] = df.apply(lambda row: calculate_days(row["Vendor Acceptance Date"], row["Installation Date"]), axis=1)
    df["Installation to Inspection Days"] = df.apply(lambda row: calculate_days(row["Installation Date"], row["Inspection Date"]), axis=1)
    df["Inspection to Subsidy Redeemed Days"] = df.apply(lambda row: calculate_days(row["Inspection Date"], row["Subsidy Redeemed Date"]), axis=1)
    df["Subsidy Redeemed to Released Days"] = df.apply(lambda row: calculate_days(row["Subsidy Redeemed Date"], row["Subsidy Released Date"]), axis=1)
    
    # Apply N/A for rejected applications
    rejected_mask = df["Acceptance Status"].str.lower() == "rejected"
    new_columns = [
        "Registration to Approval Days", "Approval to Vendor Selection Days",
        "Vendor Selection to Acceptance Days", "Acceptance to Installation Days",
        "Installation to Inspection Days", "Inspection to Subsidy Redeemed Days",
        "Subsidy Redeemed to Released Days"
    ]
    df.loc[rejected_mask, new_columns] = "N/A"
    
    # Save to new file
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

# File paths
input_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# Run preprocessing
preprocess_data(input_file, output_file)
