import random
from random import randint

area = ["Red", "middle", "Blue", "middle", "middle", "middle", "middle",
        "middle", "middle", "middle", "middle", "middle", "middle", "middle",
        "middle", "middle", "middle"]

area2 = ["middle","middle","middle","middle","middle","middle"]
neutral = None
red = ""
blue = ""
red_life = 3
blue_life = 3


class RandDice:
    # def __init__(self):
    #

    # 동전으로 선정하기
    def random_coin(self):
        c = randint(0, 1)  # 0 아니면 1
        players = ["Red", "Blue"]
        player1 = players[c]
        player2 = players - player1
    # 주사위 돌리기
    def dice_play(self):
        dice = randint(1, 6)
        # print(f'주사위의 숫자는 {dice}')
        return dice

