alist = list(map(int, input().split()))
x,y=0,0
p = False
for i in range(-999,1000):
    for j in range(-999,1000):
        if alist[0]*i+alist[1]*j == alist[2] and alist[3]*i+alist[4]*j==alist[5]:
            x = i
            y = j
            p = True
            break
    if p:
        break
        
print(x,y)