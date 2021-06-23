
def vartest(a):
    a = a+1 #지역 변수
    return a
a=1 #전역 변수
print(vartest(a))
print(a) #global a 해주면 값이 2가됌 *vartest()안에 a뺴야됌
