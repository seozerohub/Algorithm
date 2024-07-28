x = int(input())
nlist = list(map(int,input().split()))
cnt = 0
for i in nlist:
    if x == i:
       cnt +=1
print(cnt)