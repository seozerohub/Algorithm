n = int(input())
nlist = []
alist = []
blist = []
cnt = 0
result = []

for i in range(n):
    a = int(input())
    nlist.append(a)

rlist = nlist[:]

while cnt < n:
    if alist and alist[-1] == nlist[0]:
        alist.pop()
        blist.append(nlist[0])
        nlist.pop(0)
        result.append("-")
    else:
        cnt += 1
        alist.append(cnt)
        result.append("+")

while alist:
    blist.append(alist.pop())
    result.append("-")

if rlist == blist:
    print(*result, sep='\n')
else:
    print("NO")
