from pathlib import Path
import csv

#initialize the path and split text in lines
path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

#initialize csv.reader, read the header
reader = csv.reader(lines)
header_row = next(reader)

# return column names and its position
for index, column_header in enumerate(header_row):
    print(index, column_header)

#read csv data
#the highest temperatures
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)