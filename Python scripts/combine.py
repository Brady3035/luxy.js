import os
import pandas as pd

# Path to the folder containing the CSV files
folder_path = 'src/Hourly_data/Hourly Data from 2022-11-01 to 2023-02-28'

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame(columns=['Date', 'kWh', 'Building'])

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Extract building name from the filename
        building_name = os.path.splitext(filename)[0]

        # Read the CSV file into a DataFrame
        file_path = os.path.join(folder_path, filename)
        print(f"Processing file: {file_path}")

        try:
            df = pd.read_csv(file_path)

            # Add a new 'Building' column with the building name
            df['Building'] = building_name

            # Iterate through each row and append to the combined DataFrame
            for index, row in df.iterrows():
                combined_data = combined_data.append(row[['Date', 'kWh', 'Building']], ignore_index=True)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Save the combined data to a new CSV file
combined_data.to_csv('src/Hourly_data/combined_data1.csv', index=False)

print("Combining CSV files completed.")
