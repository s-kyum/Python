import pickle
#객체의 형태를 그대로 저장하고 불러오는 모듈
#바이너리 모드 사용
with open('pickle.txt','wb') as f:
    li = ['아나','토르비욘','애쉬']
    dic = {1:'사과', 2:'바나나', 3:'수박'}
    pickle.dump(li, f)
    pickle.dump(dic, f)
with open('pickle.txt','rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)