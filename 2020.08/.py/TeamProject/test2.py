from random import randint


class Player:
    def __init__(self):
        self.player1 = "RED"
        self.player2 = "BLUE"

    def rand_dice(self):
        dice_n = randint(1, 6)
        return dice_n


p1 = Player()
p2 = Player()
print(p1.player1)
print(f'{p1.player1}가 주사위를 던집니다. {p1.rand_dice()}가 나왔습니다.')
print(p2.player2)
print(f'{p2.player2}가 주사위를 던집니다. {p2.rand_dice()}가 나왔습니다.')
