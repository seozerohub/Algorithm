a = int(input())
hotel = list()
for i in range(a):
    H,W,N= map(int,input().split())
    y = (N//H)+1
    x = N%H
    if x==0:
        x=H
        y=(N//H)
    print(x*100 + y)