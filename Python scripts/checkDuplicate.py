import csv

def remove_duplicates(input_file):
    seen_lines = set()

    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    with open(input_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header to the output file
        writer.writerow(data[0])

        for row in data[1:]:
            line_string = str(row)
            if line_string not in seen_lines:
                seen_lines.add(line_string)
                writer.writerow(row)

# Example usage
input_csv = 'src/Hourly_data/combined_hourly_data_final.csv'

remove_duplicates(input_csv)
print(f"Duplicate lines removed in-place from {input_csv}.")
