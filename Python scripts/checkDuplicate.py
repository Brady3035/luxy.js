import csv
from collections import defaultdict

def remove_duplicates(input_file):
    seen_lines = set()
    output_rows = []

    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        output_rows.append(header)

        for row_num, row in enumerate(reader, start=2):  # Start from line 2 for proper numbering
            line_string = str(row)
            if line_string not in seen_lines:
                seen_lines.add(line_string)
                output_rows.append(row)

    with open(input_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output_rows)

# Example usage
input_csv = 'src/Hourly_data/combined_hourly_data_final.csv'

remove_duplicates(input_csv)
print(f"Duplicate lines removed (keeping only the first occurrence) from {input_csv}.")
