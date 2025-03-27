import pandas as pd

print("Your dataset is under preprocessing phase...")

def calculate_days(start_dates, end_dates):
    # Clean inputs
    start_dates = start_dates.str.strip().str.lower()
    end_dates = end_dates.str.strip().str.lower()
    
    # Check for "pending"
    pending_mask = start_dates.str.contains("pending", na=False) | end_dates.str.contains("pending", na=False)
    
    # Convert to datetime with explicit format if known
    start_dt = pd.to_datetime(start_dates, errors='coerce')  # Add format='%Y-%m-%d' if applicable
    end_dt = pd.to_datetime(end_dates, errors='coerce')      # Add format='%Y-%m-%d' if applicable
    
    # Initialize result as object dtype
    days_diff = pd.Series(index=start_dates.index, dtype='object')  # Explicitly set dtype to object
    
    # Calculate days difference
    days_diff[~pending_mask] = (end_dt - start_dt).dt.days + 1  # Inclusive count
    
    # Handle special cases
    days_diff[pending_mask] = "Pending"
    days_diff[start_dt.isna() | end_dt.isna()] = "N/A"
    
    return days_diff

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file, dtype=str)
    
    # Clean data and standardize statuses
    df["Acceptance Status"] = df["Acceptance Status"].str.strip().str.capitalize()
    
    # Create masks for accepted and rejected statuses
    accepted_mask = df["Acceptance Status"] == "Accepted"
    
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
    
    # Process accepted applications in a vectorized manner
    for start_col, end_col, new_col in date_pairs:
        df[new_col] = pd.Series(dtype='object')  # Initialize column as object dtype
        df.loc[accepted_mask, new_col] = calculate_days(df.loc[accepted_mask, start_col], df.loc[accepted_mask, end_col])
    
    # Set N/A for rejected applications (already handled by default value)
    
    # Handle missing values
    df.fillna("NULL", inplace=True)
    
    df.to_csv(output_file, index=False)
    print(f"Data preprocessing complete. CSV File Created: {output_file}")

# File paths
input_file = r"D:\Projects\RTS Analysis\consumer_cleaned_data.csv"
output_file = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"

# Run preprocessing
preprocess_data(input_file, output_file)
