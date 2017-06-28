count = 0
def doit(x): 
        global count 
        count = count + 1 
        return x + 1
tst = [10,19,25,18,17,23,29] 
print(tst) 
for i in range(len(tst)): 
        if tst[i] % 2 == 1: 
                tst[i] = doit(tst[i]) 
print(tst)
print('doit was called %d times.' % count) 
