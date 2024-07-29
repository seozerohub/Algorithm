a = int(input())
nlist = list(map(int, input().split()))

nset = set(nlist)

for i in range(1,a+1):
    if i not in nset:
        print(i)