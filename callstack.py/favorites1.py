import csv

# Open CSV file
with open("favorites.csv", "r") as file: #r read

    # Create readeыr
    reader = csv.DictReader(file)# передаем файл в качестве входных данных/ключ->значение

    # Skip header row
    next(reader)#пропускаем перввую строку

    # Iterate over CSV file, printing each title
    for row in reader:
        print(row["title"])
