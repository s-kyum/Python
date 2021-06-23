#dictionary

person={}
print(person)

person['name']='지우'
person['age']=20
person['출신지']='태초마을'

print(person)
for key in person:
    print(person[key])

#요소삭제 dic.pop('출신지')와 같음
del person['출신지']
print(person)
