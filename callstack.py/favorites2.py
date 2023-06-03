#  фильтруем дубликаты
import csv

titles = []# ввели переменную тайтл / список пустой
# Open CSV file
with open("favorites.csv", "r") as file: #r read
    reader = csv.DictReader(file)# передаем файл в качестве входных данных/ключ->значение
    for row in reader:
        title = row["title"].strip().upper() #Метод strip()возвращает копию строки, в которой все символы были удалены с начала и конца строки (символом по умолчанию является пробел).
        if not row["title"] in titles: #если это не тот случай когда заголовок находится в заголовках
            titles.append(title) #тогда добавляем заголовок к текущему списку

    for title in titles:
        print(title)
