N,M = map(int, input().split())
nlist = list(map(int, input().split()))
sumlist = []
tlist = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1,N):
            s = nlist[i]+ nlist[j] + nlist[k]
            if s<=M:
                sumlist.append(s)

for i in range(len(sumlist)):
    s = abs(sumlist[i]-M)
    tlist.append(s)

print(sumlist[tlist.index(min(tlist))])