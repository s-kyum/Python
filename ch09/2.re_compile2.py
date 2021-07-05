#정규 표현식 예제
import re

p = re.compile('[a-z]+')
r = p.match('2021 incheon') #결과 None / match는 처음에 일치하는 문자가 없어서 none(만약앞에 incheon이있으면 incheon 출력)
print(r)

p = re.compile('\w+ \w+')
r = p.match('2021 incheon') #공백도 문자
print(r)

s = p.search('2021 incheon') #serch는 전체 검색해서 일치하는 문자 찾음
print(s)