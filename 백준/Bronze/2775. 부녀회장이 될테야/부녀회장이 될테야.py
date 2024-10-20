t = int(input())
for k in range(t):
    a = int(input())
    b = int(input())
    blist = []
    for i in range(1, b + 1):
        blist.append(i)

    for i in range(a):
        r = 0
        for j in range(b):
            r = blist[j] + r
            blist[j] = r

    print(blist[b - 1])