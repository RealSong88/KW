import random
car = 0

car = random.randrange(1, 11)

winner = []

while True:
    temp = random.randrange(1,11)
    dupl = False
    if len(winner) == 5 :
        break
    # if car == temp:
    #     continue
    for i in winner:
        if i == temp:
            dupl = True
    if dupl:
        pass
    else:
        winner.append(temp)


print(winner)
