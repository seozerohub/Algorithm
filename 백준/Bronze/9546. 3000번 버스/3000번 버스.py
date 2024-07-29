a = int(input())

for i in range(a):
    x = int(input())
    cnt = 0
    y = 0
    while True:
        y = (y+0.5)*2
        cnt +=1
        if cnt==x:
            break
    print(int(y))