#정규 표현식 예제
import re

p = re.compile('[a-z]+') #+를 안붙히면 한개밖에 못찾음 <+>:반복을 의미하는 메타문자
r = p.match('afternoon')
print(r)

p1 = re.compile('[ca+t]')
r1=p.match('caaaaaaaaaat')
print(r1)