N,K = map(int, input().split())
nlist = list(map(int,input().split()))
Glist = []
for i in range(K):
    P = nlist[i]*100//N
    if 0<=P and P<=4:
        Glist.append(1)
    elif 4<P and P<=11:
        Glist.append(2)
    elif 11<P and P<=23:
        Glist.append(3)
    elif 23<P and P<=40:
        Glist.append(4)
    elif 40<P and P<=60:
        Glist.append(5)
    elif 60<P and P<=77:
        Glist.append(6)
    elif 77<P and P<=89:
        Glist.append(7)
    elif 89<P and P<=96:
        Glist.append(8)
    elif 96<P and P<=100:
        Glist.append(9)
print(*Glist)