#리스트의 연산

score = [70,80,50,60,90,40]
count=len(score)
print("개수 : %d개" %count)

#합계
sum=0
for i in score:
    sum += i #sum = sum + i
    print("i=%d, sum=%d" %(i,sum))
    
print("합계 : %d점" %sum)

#평균
avg=sum/len(score)
print("평균 : %.1f" %avg) #%d가 아닌 %f로(소수점반영 .1:소수점첫째자리까지)
