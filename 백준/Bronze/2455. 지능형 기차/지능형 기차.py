alist = []
blist = []
for i in range(4):
    a,b = map(int, input().split())
    alist.append(a)
    blist.append(b)

rlist = [blist[0]-alist[0], blist[0]-alist[0]+blist[1]-alist[1],
         blist[0]-alist[0]+blist[1]-alist[1]+blist[2]-alist[2],
         blist[0]-alist[0]+blist[1]-alist[1]+blist[2]-alist[2]+alist[3]-alist[3]]
print(max(rlist))