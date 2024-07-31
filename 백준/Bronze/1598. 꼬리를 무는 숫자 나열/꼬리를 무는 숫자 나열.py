a,b = map(int,input().split())
if b%4==0:
    b1 = b//4-1
else:
    b1 = b//4

if a%4==0:
    a1 = a//4-1
else:
    a1 = a//4
if a1>b1:
    a1,b1 = b1,a1
x = b1-a1

if b%4==0:
    b2 = 4
else:
    b2 = b%4
if a%4==0:
    a2 = 4
else:
    a2 = a%4

if a2>b2:
    a2,b2 = b2,a2
y = b2-a2


print(x+y)