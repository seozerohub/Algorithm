a, b = map(int, input().split())
r = a * b
if b > a:
    a, b = b, a

while True:
    if b == 0:
        break
    a = a % b
    if b > a:
        a, b = b, a
print(r // a)