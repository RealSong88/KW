import random


class Event:
                   # 회사이름, total, 당첨자 수
    def __init__(self, name, member=10):  # total 몇명인지 정한다. 기본은 10명
        self.name = name
        self.member = member
        self.num_o_p = []
        self.rank = []
        self.list_create()
        # self.ranking()

    def list_create(self):  # 번호 리스트를 만든다.
        self.num_o_p = []
        for i in range(1, self.member + 1):
            self.num_o_p.append(i)

    def ranking(self, n = 3):  # 당첨자 수 n 명을 지정, 기본 3명
        for i in range(n):
            y = random.randrange(1, len(self.num_o_p))
            self.rank.append(self.num_o_p[y])  # 0 ~ n-1 까지의 등수를 리스트로 저장.
            self.num_o_p.pop(y)

    def rank_show(self):
        print("{}의 행사 이벤트 추첨입니다.".format(self.name))
        for i in range(len(self.rank)):
            print("{0:>3}명중에 {1:>2}등은 {2:>3}번 입니다.!!".format(self.member, (i + 1), self.rank[i]))


# company_A에는 10명중에서 랭킹을 뽑는다.
if __name__ == "__main__":
    company_A = Event('company_A')
    company_A.ranking(5)
    company_A.rank_show()

    print()

    company_B = Event('company_B', 15)
    company_B.ranking(1)
    company_B.rank_show()

    print()

    company_C = Event('company_C', 20)
    company_C.ranking()
    company_C.rank_show()

    print()
    company_D = Event('company_D', 100)
    company_D.ranking(10)
    company_D.rank_show()

