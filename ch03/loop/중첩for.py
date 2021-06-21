#중첩 for
#5행 5열의 배열
for i in range(1,6):
    for j in range(1,6):
        print("가", end=" ")
    print()

#1부터 1씩 증가하기
for i in range(0,6):
    for j in range(1,6):
        print(i*5+j, end=" ")
    print()

    
#1부터 1씩 증가하기+2행만 두칸 띄기
for i in range(0,6):
    for j in range(1,6):
        if i<2 :
            print(i*5+j,end="  ")
        else:
            print(i*5+j,end=" ")
    print()
