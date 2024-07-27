s = list(input())
alist = list('abcdefghijklmnopqrstuvwxyz')
count = [0]*26
for i in s:
    for j in range(26):
        if i == alist[j]:
            count[j]+=1
print(*count)