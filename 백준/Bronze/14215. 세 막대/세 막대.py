a,b,c = map(int, input().split())
nlist = [a,b,c]
nlist.sort()

a = nlist[0]
b = nlist[1]
c = nlist[2]

if a+b>c :
    print(a+b+c)
else:
    r = c - (a+b) +1
    r = c - r
    print(r + a + b)