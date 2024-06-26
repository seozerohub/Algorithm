n = int(input())
nlist = list(map(int, input().split()))
t,p = map(int, input().split())

sum=0
for i in nlist:
    if i%t==0:
        x= i//t
        sum += x
    else:
        x = i//t
        x +=1
        sum += x

mok = n//p
let = n%p
print(sum)
print(mok,let)