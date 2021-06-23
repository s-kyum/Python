#리스트의 최대값,최소값,정렬

score=[70,80,50,60,90,45]
n=len(score)
max=score[0]
score.sort()
print(score)
for i in range(1,n):
    if max < score[i]:
        max=score[i]

print(max)

#오름차순 정렬
for i in range(0,n):
    for j in range(0,n-1):
        if score[j]>score[j+1]:
            score[j],score[j+1]=score[j+1],score[j]

for i in score:
    print(i,end=' ')
