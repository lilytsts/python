def square_digits(num):
    result =  "" #инициируем переменную резалт равную пучстой строке 
    string = str(num)
    for i in string:
        result += str(int(i)**2)#приводим в строковый тип чтобы была канкотенация строк если не перевести в строковый тип получится сумма чилел

    return int(result)
