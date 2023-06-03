# Prints all titles in CSV using csv.reader

import csv

# Open CSV file
with open("favorites.csv", "r") as file: #r read

    # Create reader
    reader = csv.reader(file)# передаем файл в качестве входных данных

    # Skip header row
    next(reader)#пропускаем перввую строку

    # Iterate over CSV file, printing each title
    for row in reader:
        print(row[1])
