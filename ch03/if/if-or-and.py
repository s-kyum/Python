#현금 또는 카드가 있으면 택시를 타고 아니면 걸어간다.

money=3000
card = True #첫글자 대문자
if money >=3000 or not card:
    print("택시를 탄다")
else :
    print("걸어간다")

poket =['paper','스마트폰','money']
if 'money' and 'coin' in poket:
    print('택시를 탄다')
else:
    print('걸어간다')
