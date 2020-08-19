from mymodify.dice.user import User
from random import randint


class Game:
    def __init__(self):
        self.persons = 0
        self.start_life = 0
        self.map_size = 6
        # self.users 에 User 객체가 들어가 있다.
        self.users = []
        self.land = []
        for i in range(self.map_size):
            self.land.append("")
        self.start()

    def start(self):
        print("랜덤 다이스에 오신것을 환영합니다~!. 게임을 시작하겠습니다.")

        # input(persons map_size start_life)
        # ex) 2 17 3
        input_result = input("인원 수, 목숨을 입력해주세요\nex)2 3\n")
        input_list = input_result.split(" ")

        # Game(persons, start_life)
        self.persons = int(input_list[0])
        self.start_life = int(input_list[1])

        self.input_name()

    # 닉네임 입력 함수
    def input_name(self):
        # User 닉네임 입력
        for i in range(self.persons):
            user_name = input("{}번째 유저의 닉네임을 입력하세요\n".format(i + 1))
            self.users.append(User(user_name, self.start_life))

    # 선공 정하기 함수
    def toss_coin(self):
        result = randint(0, 1)
        return result

    def game_over(self):
        temp_list = []
        land_set = set(self.land)

        print("\n")

        for i in land_set:
            temp_list.append([i, self.land.count(i)])

        for i in range(len(temp_list)):
            if temp_list[i][0] == "":
                print("미점령된 땅의 개수 - {0}".format(temp_list[i][1]))
            else:
                print("{0}님의 땅의 개수 - {1}".format(temp_list[i][0], temp_list[i][1]))

        # 변수에 승자 땅 갯수, 승자명 담기
        land_count = 0
        winner = ""
        for i in land_set:
            if i == "": continue

            # 처음일 때,
            if land_count == 0:
                winner = i
                land_count = self.land.count(i)
                continue

            # 땅의 갯수가 같을때
            if land_count == self.land.count(i):
                winner = winner + ",{}".format(i)
            # 땅의 갯수가 더 많을때
            elif land_count < self.land.count(i):
                winner = i
                land_count = self.land.count(i)

        # 비겼을 때
        if winner.find(",") != -1:
            print("\n비겼습니다!\n")
            return
        # 결과가 나왔을 때
        print("\n{0}님이 승리하셨습니다!\n".format(winner))
