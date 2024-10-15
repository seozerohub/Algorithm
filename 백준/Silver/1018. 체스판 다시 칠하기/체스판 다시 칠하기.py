n, m = map(int, input().split())
alist = []
result = []
for i in range(n):
    alist.append(input())

for a in range(n-7):
    for b in range(m-7):
        cntB = 0
        cntW = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)% 2 == 0:
                    if alist[i][j] !='B':
                        cntB = cntB + 1
                    if alist[i][j] !='W':
                        cntW = cntW + 1
                else:
                    if alist[i][j] !='W':
                        cntB = cntB +1
                    if alist[i][j] !='B':
                        cntW = cntW + 1
        result.append(cntB)
        result.append(cntW)


print(min(result))