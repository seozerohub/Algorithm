alist = []
for i in range(5):
    a = int(input())
    alist.append(a)

x = alist[1]//alist[3]
x1 = alist[1]%alist[3]
y = alist[2]//alist[4]
y1 = alist[2]%alist[4]
if x1==0:
    x = x
else:
    x = x+1

if y1==0:
    y = y
else:
    y = y+1

if x>y:
    r = alist[0]-x
else:
    r = alist[0]-y
print(r)