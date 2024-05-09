n = int(input())
xlist=[]
ylist=[]

for i in range(n):
    x,y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)

x = max(xlist) - min(xlist)
y = max(ylist) - min(ylist)

print(x*y)