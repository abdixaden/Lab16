import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Load the data
dates = []
rates = []

with open('OHUR.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Analyze header with enumerate
    for i, row in enumerate(reader):
        print(f"{i}: {row}")
        # Skip the header
        if i == 0:
            continue
        if len(row) == 2 and row[1] != '.':  # Ensure valid data
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
            dates.append(date)
            rates.append(rate)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(dates, rates, color='blue', linewidth=1)
plt.title('National Unemployment Rate (1976 - Present)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
