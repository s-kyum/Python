#영어 단어 저장하기

f = open("words.txt",'a')
word = ['winston','ashe','ana','mercy','sigma','diva','soldier','echo','sombra','rodhog','bastion']
for i in word:
    f.write(i + " ")
f.close()