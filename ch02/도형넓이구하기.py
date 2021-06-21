#도형의 넓이 계산하기

#1.한 변의 길이가 5cm인 정사각형의 넓이
size = int(input("정사각형의 한변의 길이 : "))
area = size*size
#print("정사각형의 넓이 : ",area,"cm")
print("정사각형의 넓이 : %dcm" %area)

#2.한 변의 길이가 5cm이고 높이 7cm인 삼각형의 넓이
width = int(input("삼각형의 가로길이 : "))
height = int(input("삼각형의 높이 : "))
area=width*height/2
#print("삼각형의 넓이 : ",area,"cm")
print("삼각형의 넓이 : %dcm" %area)


'''
%d = 정수
%s = 문자
%f = 소수
'''
