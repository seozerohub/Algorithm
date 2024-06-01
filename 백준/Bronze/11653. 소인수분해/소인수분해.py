a = int(input())
nlist = []

def prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

t = 2
while True:
    if a==1:
        break
    elif a % t == 0:
        a = int(a / t)
        nlist.append(t)
        if prime(a) == True:
            nlist.append(a)
            break
    else:
        t += 1

if nlist == []:
    pass
else:
    nlist.sort()
    for i in nlist:
        print(i)