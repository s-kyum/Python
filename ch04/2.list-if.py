#리스트를 이용한 합격판정
#점수가 60점 이상이면 합격 else 불합격

score = [70,80,50,60,90,45]
index = 0
for i in score:
    index +=1
    if i >= 60:
        print("%d번 학생은 합격입니다." %index)
    else:
        print("%d번 학생은 불합격입니다." %index)

print('='*40)

print("for in range() 구문")

n = len(score)
for i in range(0, n):
    if score[i] >= 60: #i는 정수가 아니라 인덱스가 되었기때문(리스트의값)
        print("%d번 학생은 합격입니다." %(i+1)) #대응변수()로묶음.
    else:
        print("%d번 학생은 불합격입니다." %(i+1))
