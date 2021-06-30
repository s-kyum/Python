#파일 열기(open) -> 파일쓰기(write) -> 파일 닫기(close)

f = open('C:/pyfile/hello.txt','w')  #쓰기는 w 읽기는 r
f.write('hello~python')
#f.write(1000) 그냥 숫자는 입력안됌
f.write('\n%d\n'%1000)  #\n : 한줄 띄기
num = "%d\n" % 100    #\t : 한칸 띄기
f.write(num)
f.write('%.1f'%2.5)
f.write("\n윈스턴")
f.close()