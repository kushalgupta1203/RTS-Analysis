import pandas as pd

print("Your dataset is under preprocessing phase...")

def calculate_days(start_date, end_date):
    # Convert to string and clean inputs
    start_str = str(start_date).strip().lower() if pd.notna(start_date) else ""
    end_str = str(end_date).strip().lower() if pd.notna(end_date) else ""
    
    # Pending check
    if "pending" in [start_str, end_str]:
        return "Pending"
    
    # Date conversion check
    try:
        start_dt = pd.to_datetime(start_str, format="%d-%m-%Y", errors='coerce')
        end_dt = pd.to_datetime(end_str, format="%d-%m-%Y", errors='coerce')
        
        if pd.isna(start_dt) or pd.isna(end_dt):
            return "N/A"
            
        return (end_dt - start_dt).days + 1  # Inclusive count
    except:
        return "N/A"

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file, dtype=str)
    
    # Clean data
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Create masks
    accepted_mask = df["Acceptance Status"].str.lower() == "accepted"
    rejected_mask = df["Acceptance Status"].str.lower() == "rejected"
    
    # Define date pairs
    date_pairs = [
        ("Registration Date", "Application Approved Date", "Registration to Approval Days"),
        ("Application Approved Date", "Vendor Selection Date", "Approval to Vendor Selection Days"),
        ("Vendor Selection Date", "Vendor Acceptance Date", "Vendor Selection to Acceptance Days"),
        ("Vendor Acceptance Date", "Installation Date", "Acceptance to Installation Days"),
        ("Installation Date", "Inspection Date", "Installation to Inspection Days"),
        ("Inspection Date", "Subsidy Redeemed Date", "Inspection to Subsidy Redeemed Days"),
        ("Subsidy Redeemed Date", "Subsidy Released Date", "Subsidy Redeemed to Released Days")
    ]
    
    # Process accepted applications
    for start_col, end_col, new_col in date_pairs:
        df[new_col] = "N/A"  # Default value
        df.loc[accepted_mask, new_col] = df.loc[accepted_mask].apply(
            lambda row: calculate_days(row[start_col], row[end_col]), axis=1
        )
    
    # Set N/A for rejected applications
    new_columns = [col[2] for col in date_pairs]
    df.loc[rejected_mask, new_columns] = "N/A"
    
    # Handle missing values
    df.fillna("NULL", inplace=True)
    
    df.to_csv(output_file, index=False)
    print(f"Data preprocessing complete. CSV file created: consumer_preprocessed_data.csv")

# File paths
input_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# Run preprocessing
preprocess_data(input_file, output_file)
