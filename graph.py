import csv

with open('OHRU.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header row
    for index, column_name in enumerate(header):
        print(f"Column {index}: {column_name}")