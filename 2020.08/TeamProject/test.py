from random import randint

area2 = ["middle", "middle", "middle", "middle", "middle", "middle"]
area3 = ["Red", "Red", "Red", "Red", "Red", "Red"]
area4 = ["Blue", "Blue", "Blue", "Blue", "Blue", "Blue"]


player1 = []
player2 = []
red_life = 3
blue_life = 3
coin = randint(0, 1)
if coin == 0:  # 0이면 Red 가 선
    player1 = ["Red", 3]
    player2 = ["Blue", 3]
else:  # 1 이면 Blue 가 선
    player1 = ["Blue", 3]
    player2 = ["Red", 3]

print("*" * 55)
print("{0:*^50}".format("게임을 시작합니다"))
input("선을 정합니다. 동전을 던지세요.(enter)")
print(f"{player1[0]}가 선입니다")
while player1[1] != 0 and player2[1] != 0:

    input(f"{player1[0]}의 차례입니다. 주사위를 던지세요.(enter)")
    dice = randint(1, 6)
    move = dice - 1
    print(f"주사위 {dice} 칸 이동")

    if area3[move] == "middle":
        area3[move] = player1[0]
        print("땅을 점령하셨습니다.")
    elif area3[move] == player2[0]:
        print("남의 땅을 밝으셨네요 생명력이 깎입니다.")
        player1[1] -= 1
    else:
        print("자기땅입니다.")
    print(f"{player1[0]} 잔여 생명력 {player1[1]}")
    if player1[1] == 0:
        break

    input(f"{player2[0]}의 차례입니다. 주사위를 던지세요.(enter)")
    dice = randint(1, 6)
    move = dice - 1
    print(f"주사위 {dice} 칸 이동")

    if area3[move] == "middle":
        area3[move] = player2[0]
        print("땅을 점령하셨습니다.")
    elif area3[move] == player1[0]:
        print("남의 땅을 밝으셨네요 생명력이 깎입니다.")
        player2[1] -= 1
    else:
        print("자기땅입니다.")
    print(f"{player2[0]} 잔여 생명력 {player2[1]}")
