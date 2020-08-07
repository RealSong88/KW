import random

area = ["Red", "middle", "Blue", "middle", "middle", "middle", "middle",
        "middle", "middle", "middle", "middle", "middle", "middle", "middle",
        "middle", "middle", "middle"]

area2 = ["Red","Red","Red","Red"]
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
        c = random.randrange(2)  # 0 아니면 1
        if c == 0:
            result = "Red"
        else:
            # print("Blue가 선!")
            result = "Blue"
        return result
    # 주사위 돌리기
    def dice_play(self):
        dice = random.randrange(1, 7)
        # print(f'주사위의 숫자는 {dice}')
        return dice

# area[1] = "red"
# print(area)

p1 = RandDice()
# print(p1.random_coin())

# print(p1.dice_play())
print(area2)
while True:
        now_player = p1.random_coin()
        print(now_player)
        dice = random.randrange(1, 4)
        move = dice - 1
        print(dice)
        for i in range(len(area)):
                if area[move] == "middle":
                        area2[move] = now_player
                # elif area2[move] == "middle":
                #         area2[move] = now_player
                elif area2[move] == "Red":
                        if now_player != "Red":
                            print("Blue 생명 -1,남은 생명 ")
                            break
                        else:
                               pass

        break

print(area2)
# a = RandDice()
# a.random_coin()
# a.dice_play()
# print(input(("""
#         동전의 앞면은 Red, 뒷면은 Blue
#         동전을 던져주세요 >> press....
#       """)))
