import os
import pandas as pd

# Path to the folder containing the CSV files
folder_path = 'src\Hourly_data'

# Create an empty list to store the combined data
combined_data_list = []

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

        

            # Iterate through each row and append to the combined data list
            for index, row in df.iterrows():
                combined_data_list.append(row[['Date', 'kWh', 'Building']].tolist())
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Convert the list to a DataFrame
combined_data = pd.DataFrame(combined_data_list, columns=['Date', 'kWh', 'Building'])

# Save the combined data to a new CSV file
combined_data.to_csv('src/Hourly_data/combined_hourly_data_final.csv', index=False)

print("Combining CSV files completed.")
