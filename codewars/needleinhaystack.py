def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == 'needle':
            return f'found the needle at position {index}'
        index +=1
        
