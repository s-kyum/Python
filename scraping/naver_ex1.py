from urllib import request
from bs4 import BeautifulSoup
html = request.urlopen("https://www.naver.com/")
contents = BeautifulSoup(html,'html.parser')
top_right = contents.find('div',{'class':'service_area'})
naver = top_right.find('a')
print(naver)
print(naver.text)