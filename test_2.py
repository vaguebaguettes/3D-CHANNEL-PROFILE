import csv

def extract_and_delete_column(input_csv, output_csv, column_name):
    try:
        # Read the input CSV and write the output CSV
        with open(input_csv, "r") as infile, open(output_csv, "w", newline="") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            # Write the header for the output CSV
            writer.writerow([column_name])

            rows = list(reader)
            for row in rows:
                # Extract the desired column value
                column_value = row.get(column_name)
                writer.writerow([column_value])

        # Remove the column from the original CSV
        with open(input_csv, "w", newline="") as infile:
            fieldnames = [fn for fn in rows[0].keys() if fn != column_name]
            writer = csv.DictWriter(infile, fieldnames=fieldnames)

            # Write the header and rows without the extracted column
            writer.writeheader()
            for row in rows:
                del row[column_name]
                writer.writerow(row)

        print(f"Column '{column_name}' extracted to '{output_csv}' and deleted from '{input_csv}' successfully.")
    except FileNotFoundError:
        print(f"File '{input_csv}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



