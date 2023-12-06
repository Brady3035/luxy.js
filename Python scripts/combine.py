import os
import pandas as pd

# Path to the folder containing the CSV files
folder_path = '/path/to/your/csv/files/'

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame(columns=['Date', 'kWh', 'Building'])

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Extract building name from the filename
        building_name = os.path.splitext(filename)[0]

        # Read the CSV file into a DataFrame
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        # Add a new 'Building' column with the building name
        df['Building'] = building_name

        # Append the data to the combined DataFrame
        combined_data = combined_data.append(df[['Date', 'kWh', 'Building']], ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('src/Hourly_data/combined_data.csv', index=False)

print("Combining CSV files completed.")
