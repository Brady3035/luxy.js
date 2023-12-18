import csv

def filter_csv(input_file, output_file, search_string):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        # Initialize CSV reader and writer
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        # Read and write the header row
        header = next(csv_reader)
        csv_writer.writerow(header)

        # Iterate through each line in the input CSV
        for row in csv_reader:
            # Check if the search string is in the line
            if any(search_string.lower() in cell.lower() for cell in row):
                csv_writer.writerow(row)

if __name__ == "__main__":
    # Provide the paths and the search string
    input_csv_path = 'src/Hourly_data/academic_sq2_2022-2023_hourly.csv'
    output_csv_path = 'src/Hourly_data/academic_sq_2022_hourly.csv'
    search_string = '2022-11-0'  # Replace with the string you're searching for

    # Call the function to filter the CSV
    filter_csv(input_csv_path, output_csv_path, search_string)

    print(f"Filtering completed. Results saved to {output_csv_path}")
