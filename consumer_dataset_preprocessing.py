import pandas as pd

print("Your dataset is under preprocessing phase...")

def calculate_days(start_date, end_date):
    # Clean inputs
    start_str = str(start_date).strip() if pd.notna(start_date) else ""
    end_str = str(end_date).strip() if pd.notna(end_date) else ""
    
    # Check for "pending"
    if "pending" in [start_str.lower(), end_str.lower()]:
        return "Pending"
    
    # Attempt to convert to datetime
    try:
        start_dt = pd.to_datetime(start_str, errors='coerce')
        end_dt = pd.to_datetime(end_str, errors='coerce')
        
        # Check for NaT (Not a Time)
        if pd.isna(start_dt) or pd.isna(end_dt):
            return "N/A"
        
        # Calculate days difference
        return (end_dt - start_dt).days + 1  # Inclusive count
    except Exception as e:
        print(f"Error parsing dates: {e}")
        return "N/A"

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file, dtype=str)
    
    # Clean data and standardize statuses
    df["Acceptance Status"] = df["Acceptance Status"].str.strip().str.capitalize()
    
    # Create masks for accepted and rejected statuses
    accepted_mask = df["Acceptance Status"] == "Accepted"
    rejected_mask = df["Acceptance Status"] == "Rejected"
    
    # Define date pairs for calculations
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
    print(f"Data processed successfully. Output: {output_file}")

# File paths
input_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# Run preprocessing
preprocess_data(input_file, output_file)
