a = int(input())
alist = []
t = True
for i in range(1,a+1):
    alist = list(str(i))
    r = 0
    for j in range(len(alist)):
        r = int(alist[j])+r
    if int(i)+r==a:
        t = False
        print(i)
        break
if t:
    print(0)