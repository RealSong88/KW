from mymodify.menu.menu import Menu

if __name__ == "__main__":
    while True:
        input_start = input("사용하실 메뉴를 골라주세요.\n1.시작하기\n2.불러오기\n3.나가기\n")

        new_menu = Menu(input_start)

        if new_menu.now_page == "1":
            new_menu.page1()
        elif new_menu.now_page == "2":
            new_menu.page2()
        elif new_menu.now_page == "3":
            print("종료합니다.")
            break

