import random
from random import randint
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

# win = []
#
# while len(win) != 4 :
#     dice = randint(1, 6)
#     while dice in win:
#         dice = randint(1, 6)
#     win.append(dice)
#
# print(win)