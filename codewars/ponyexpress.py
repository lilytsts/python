def riders(stations):
    summ = 0
    counter = 1
    for i in stations:
        summ += i
        if summ > 100:
            counter += 1
            summ = i

    return counter
