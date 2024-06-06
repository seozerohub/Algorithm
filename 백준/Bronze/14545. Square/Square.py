a = int(input())
for i in range(a):
    n = int(input())
    cnt = 0
    for j in range(1,n+1):
        cnt = cnt+j**2
    print(cnt)