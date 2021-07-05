import re

p = re.compile('blue|red')
s= p.sub('A', 'blue socks and red shoes')  #sub() - B를 A로 변경
print(s)