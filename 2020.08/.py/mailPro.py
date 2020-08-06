names = ["로건", "피지컬갤러리", "지피티", "호우"]


def write_mail(names):
    for i in names:
        with open("{}.txt".format(i), 'w', encoding="utf8") as f:
            f.write('''
    안녕하세요? {names}님.

    (주)나도출판 편집자 나코입니다.
    현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
    {names}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
    자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

    좋은 하루 보내세요 ^^
    '''.format(names=i))


write_mail(names)
