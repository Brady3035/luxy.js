import os
import pandas as pd

def add_columns_to_csv(file_path):
    # Read the CSV file into a DataFrame without header
    df = pd.read_csv(file_path, header=None)

    # Add 'Date' and 'kWh' columns at the top of the DataFrame
    df.columns = ['Date', 'kWh'] + list(df.columns[2:])  # Assuming the rest of the columns are data

    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Path to the root folder containing the CSV files
root_folder_path = '/Users/brady3035/Documents/Comp-435/luxyproject.js/src/Hourly_data'

# Recursively find all CSV files in the root folder and its subdirectories
for foldername, subfolders, filenames in os.walk(root_folder_path):
    for filename in filenames:
        if filename.endswith('.csv'):
            file_path = os.path.join(foldername, filename)
            add_columns_to_csv(file_path)

print("Adding 'Date' and 'kWh' columns completed.")

