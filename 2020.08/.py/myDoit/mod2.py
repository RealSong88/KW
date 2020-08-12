from random import randint

answer = []

while len(answer) != 4:
    new_number = randint(0, 9)
    if new_number not in answer:
        answer.append(new_number)


print(answer)