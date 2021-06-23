# abs(x) 직접 정의
'''
#절대값 알고리즘1
def abs_sign(x):
    if x<0:
        return -x
    else:
        return x
#절대값 알고리즘2
def abs_sign(x):
    if x<0:
      x = -(x)
    return x
'''    
#절대값 알고리즘3
import math
def abs_square(x):
    y=x*x
    return math.sqrt(y)

n2 = abs_square(-10)
print(n2)
#n1 = abs_sign(5)
print(n1)
