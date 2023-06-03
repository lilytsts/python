def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_summ = 0
    if not arr: #если список пустой возвращаем пустой список
        return[]
    for i in arr:
        if i>0:
            positive_count +=1 
        elif i<0:
            negative_summ += i
    return [positive_count, negative_summ]
