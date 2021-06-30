try:
    f=open('c:/pyfile/hello.txt','r')
    data = f.read()    #파일을 python 콘솔창에서 볼 수 있음
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")