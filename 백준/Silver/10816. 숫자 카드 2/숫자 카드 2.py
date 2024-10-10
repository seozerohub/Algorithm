a = int(input())
alist = list(map(int,input().split()))
b = int(input())
blist = list(map(int, input().split()))
nlist = []
d = dict()
for i in alist:
    if i in d:
        d[i] = d[i] +1
    else:
        d[i]=1

for i in blist:
    if i in d:
        nlist.append(d[i]) # d[i] = d.get(i)
    else:
        nlist.append(0)
print(*nlist)