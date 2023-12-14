import pandas as pd

def check_missing_values(csv_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Check for missing values (NaN or empty strings) in the DataFrame
    missing_values = df.applymap(lambda x: x == '' or pd.isna(x)).any(axis=1)

    # Print rows with missing values
    if any(missing_values):
        print("Rows with missing values:")
        print(df[missing_values])
    else:
        print("No rows with missing values found.")

if __name__ == "__main__":
    # Replace 'your_file.csv' with the actual path to your CSV file
    csv_file_path = 'src\Hourly_data\combined_hourly_data_final.csv'

    check_missing_values(csv_file_path)
