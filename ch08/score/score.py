
with open('scorelist.txt', 'w') as f:
    while True:
        try:
            if q == "y" or q =='Y':
                name = input("이름입력 : ")
                kor = int(input("국어점수 : "))
                math = int(input("수학점수 : "))
                avg = (kor + math) / 2
                q = str(input("성적을 저장할까요? (y/n)"))

                f.write(name + ' ')
                f.write(str(kor) + ' ')
                f.write(str(math) + ' ')
                #f.write(str(avg) + '\n')
            elif q == "n" or q == 'N':
                print("취소되었습니다.")
                break
            else:
                print("잘못된 입력입니다.")
        except ValueError:
            print("잘못된 입력입니다.")




#반복작업
#성적을 저장할까요?(y/n)
#'y'를 누르면 입력처리
#'n'을 누르면 입력종료
#다른키 누르면 "잘못된 입력입니다."