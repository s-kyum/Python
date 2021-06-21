#조건 : 15세 이상이면 드라마 관람가 이고 아니면 드라마 관람불가 출력
age = int(input("나이를 입력하세요. : "))
if age>15 :
    print("드라마 관람 가능")
    print("나이는 %d세입니다."%age)
else:
    print("드라마 관람 불가")
    print("나이는 %d세입니다."%age)

    
#놀이 공원 입장료계산
age=int(input("나이를 입력하세요. :"))
charge =0
if age<12:
    charge=2000
elif age<15:
    charge=3000
elif age<19:
    charge=4000
else:
    charge=5000
   
print("입장료 가격은 %d원 입니다." %charge) #중복 구문은 따로 뺴놓으면 전체 처리 가능
