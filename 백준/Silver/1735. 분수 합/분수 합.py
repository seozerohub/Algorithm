a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
x = b1
y = b2
r = b1*b2
if b1 > b2:
    b1,b2 = b2,b1

while True:
    if b1==0:
        break
    b2 = b2%b1
    if b1>b2:
        b1,b2 = b2,b1

bunmo = r//b2
x = bunmo//x
y = bunmo//y
bunja = a1*x+a2*y
a = bunja
b = bunmo

if bunja > bunmo:
    bunja, bunmo = bunmo, bunja

while True:
    if bunja==0:
        break
    bunmo = bunmo%bunja
    if bunja>bunmo:
        bunja,bunmo = bunmo,bunja

print(a//bunmo,b//bunmo)