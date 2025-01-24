import plottercontour

import pandas as pd

def add_headers_to_existing_csv(file_path):
    # Read the existing CSV file (assuming it already has data)
    try:
        existing_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Add headers if they don't already exist
    headers = ['x', 'y', 'z']
    for header in headers:
        if header not in existing_data.columns:
            existing_data[header] = None

    # Write the updated DataFrame back to the same file
    existing_data.to_csv(file_path, index=False)

    print(f"Headers added to existing CSV file at {file_path}")

# Specify the path to your existing CSV file
existing_csv_path = 'datas.csv'
add_headers_to_existing_csv(existing_csv_path)

plottercontour.plot('datas.csv')