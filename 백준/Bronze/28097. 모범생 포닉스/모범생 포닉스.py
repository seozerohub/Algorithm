a = int(input())
alist = list(map(int,input().split()))
r = sum(alist)
if a ==1:
    r = r
else:
    r = r+(a-1)*8

print(r//24, r%24)