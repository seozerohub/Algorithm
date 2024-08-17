x = int(input())
a,b,c = map(int,input().split())
alist = [a,b,c]
sum = 0
for i in alist:
    if i>=x:
        sum=sum+ x
    else:
        sum=sum+ i
print(sum)