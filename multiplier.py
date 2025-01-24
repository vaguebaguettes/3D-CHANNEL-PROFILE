import csv

def multiply_column(input_csv, output_csv, column_name, multiplier):
    try:
        with open(input_csv, "r") as infile, open(output_csv, "w", newline="") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            # Write the header
            writer.writerow(reader.fieldnames)

            for row in reader:
                # Multiply the column value (except for the header)
                original_value = float(row.get(column_name))
                updated_value = original_value * multiplier
                row[column_name] = updated_value
                writer.writerow(row.values())

        print(f"Column '{column_name}' multiplied by {multiplier} and saved to '{output_csv}' successfully.")
    
    except FileNotFoundError:
        print(f"File '{input_csv}' not found.")

def merge_csv_into_second_column(source_csv, target_csv):
    import pandas as pd

    # Read the first CSV file which contains the single column 'y'

    df1 = pd.read_csv(source_csv)

    # Read the second CSV file which contains the columns 'x' and 'z'

    df2 = pd.read_csv(target_csv)

    # Insert the 'y' column from the first DataFrame into the second DataFrame next to 'x'

    df2.insert(1, 'y', df1['y'])

    output = 'outputtest.csv'

    # Save the modified DataFrame back to a new CSV file
    
    df2.to_csv(output, index=False)
    return output
