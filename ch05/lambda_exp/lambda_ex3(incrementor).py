
def incrementor(n):
    return lambda x : x+n

f = incrementor(10)  #n값 = 10
print(f(1))  # x값 = 1