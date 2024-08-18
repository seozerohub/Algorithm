a,b = map(int,input().split())
xlist = list(map(int,input().split()))
cnt = 0
for i in xlist:
    if i<=b:
        cnt= cnt+1
print(cnt)