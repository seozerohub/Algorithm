dlist = dict()
alist = []
for i in range(10):
    d = int(input())
    alist.append(d)

for i in alist:
    if i in dlist:
        dlist[i]= dlist[i]+1
    else:
        dlist[i]=1

max = max(dlist, key= dlist.get)

print(sum(alist)//10)
print(max)