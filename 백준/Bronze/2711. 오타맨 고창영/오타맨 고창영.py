a = int(input())
for i in range(a):
    a,b = input().split()
    a = int(a)
    if a == 1:
        print(b[a::])
    elif a== len(b):
        print(b[0:a-1])
    else:
        print(b[0:a-1]+b[a::])