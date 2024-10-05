a = int(input())
alist = []
for i in range(a):
    alist.append(list(map(int,input().split())))

for i in alist:
    rank = 1
    for j in alist:
        if i[0]<j[0] and i[1]<j[1]:
            rank= rank+1
    print(rank, end=' ')