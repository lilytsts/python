from cs50 import get_int
scores = [] # пустой список  scores
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)# append -добавить

average = sum(scores) / len(scores)
print(f"Average: {average}")
