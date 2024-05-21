a = int(input())
slist = []
rlist = []
for i in range(a):
    s = input()
    slist.append(s)
slist = list(set(slist))

for i in range(len(slist)):
    rlist.append([slist[i]])

rlist.sort(key= lambda x: (len(x[0]), x[0]))
for i in rlist:
    print(*i)