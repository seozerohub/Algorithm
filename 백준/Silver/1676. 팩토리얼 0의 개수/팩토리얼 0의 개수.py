r = int(input()) 
n =1
for i in range(1,r+1):
    n = n*i

# 소수 판별식
def prime(a): #7
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True

# 소인수분해
p = 2
alist = []
while True:
    if n<2:
        break
    elif n%p==0: 
        n= n//p
        alist.append(p)
        if prime(n)==True: 
            alist.append(n)
            break
    else:
        p = p+1

cnt=0
cnt1=0
for i in alist:
    if i == 2:
        cnt = cnt+1
    if i==5:
        cnt1 = cnt1+1

if cnt<cnt1:
    print(cnt)
else:
    print(cnt1)
