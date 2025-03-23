import pandas as pd
import matplotlib.pyplot as plt

# Load the extracted data
file_path = r"D:\Projects\RTS Analysis\consumer_preprocessed_data.csv"
data = pd.read_csv(file_path)

# Ensure date columns are parsed correctly
date_columns = [
    'Registration Date',
    'Application Approved Date',
    'Vendor Selection Date',
    'Vendor Acceptance Date',
    'Installation Date',
    'Inspection Date',
    'Claim Submission Date',
    'Claim Release Date'
]

for col in date_columns:
    data[col] = pd.to_datetime(data[col], errors='coerce')

# 1. State-wise Total Applications Bar Graph with Ranking
state_wise_data = data.groupby('State Ut')['Application Number'].count().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
state_wise_data.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('State-wise Total Applications with Ranking', fontsize=14)
plt.xlabel('State/UT', fontsize=12)
plt.ylabel('Total Applications', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the state-wise graph
state_graph_path = r"D:\Projects\RTS Analysis\state_wise_applications.png"
plt.savefig(state_graph_path)
plt.show()

# 2. Monthly Bar Graphs for Each Date Column
for col in date_columns:
    monthly_data = data[col].dt.to_period('M').value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    monthly_data.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title(f'Monthly Applications for {col}', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Number of Applications', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save each monthly graph
    monthly_graph_path = f"D:\\Projects\\RTS Analysis\\monthly_applications_{col.replace(' ', '_').lower()}.png"
    plt.savefig(monthly_graph_path)
    plt.show()
