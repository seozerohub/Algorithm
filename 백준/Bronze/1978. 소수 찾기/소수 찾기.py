n = int(input())
nlist = list(map(int, input().split()))

alist = []
for a in nlist:
    p = True
    if a<2:
        p = False
    else:
        for i in range(2,a):
            if a%i==0:
                p = False
        if p:
            alist.append(a)

print(len(alist))