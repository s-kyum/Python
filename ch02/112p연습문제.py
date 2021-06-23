#Phython교재 112p 연습문제

#1.홍길동씨의 평균 점수 구하기
sub1=80
sub2=75
sub3=55
sum=sub1+sub2+sub3
average=(sum/3)
print(average)

#2.자연수 13이 홀수인지 짝수인지 판별
n =13
if n%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#3.홍길동씨의 주문등록번호를 연월일 부분과 숫자부분으로 나누어출력

pin="881120-1068234"
yyyymmdd=pin[0:6]
num=pin[7:]
print(yyyymmdd)
print(num)

#4.주민번호에서 성별을 나타내는 숫자를 출력
pin = "881120-1068234"
gender = pin[7]
if gender=='1':
    print("남자 입니다.")
else:
    print("여자 입니다.")

#5.문자열 교체
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6.리스트 내림차순 정렬
a=[1,3,5,4,2]
a.sort()
a.sort(reverse=True)
print(a)

#7.리스트를 문자열로 변환
a=['life','is','too','short']
result=" ".join(a)
print(result)


#split() 예제 - 문자열을 리스트로 변환
s='Life is too short'
s=s.split(' ') #구분기호 : 공백
print(s)

s="a:b:c:d"
s=s.split(':')
print(s)

#8.튜플에 값 추가
a=(1,2,3)
a=a+(4,)
print(a)

#9.dictionary
a=dict()
a['name']='python'
a[('a',)]='python'
print(a)

#10.dictinary 추출
a={'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

#11.리스트 중복제거
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)
