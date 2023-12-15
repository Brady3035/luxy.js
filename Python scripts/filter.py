import csv

def filter_and_append(input_file, output_file, buildings_to_keep):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Copy header to the new file
        header = next(reader)
        writer.writerow(header)

        # Specify the column index for the 'building' column
        building_column_index = header.index('building')

        for row in reader:
            # Check if the building is in the list
            if row[building_column_index] in buildings_to_keep:
                writer.writerow(row)

# Example usage
input_csv = 'src/Hourly_data/combined_hourly_data_final.csv'
output_csv = 'src/Hourly_data/stadium_2022-2023_hourly.csv'
buildings_to_keep = ["Stadium Field Light Electricity Meter",]

filter_and_append(input_csv, output_csv, buildings_to_keep)
print(f"Rows with specified buildings appended to {output_csv}.")
