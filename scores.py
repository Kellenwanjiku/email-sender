from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score) #you can also do scores += [score]

average = sum(scores)/ len(scores)
print(f"Average: {average}")