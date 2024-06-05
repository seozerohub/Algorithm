import sys
input = sys.stdin.readline
a = input().rstrip()
a = int(a)
cnt = 0
for i in range(a):
    n = list(input().rstrip())
    for j in range(len(n)-1):
        if n[j] == '0' and n[j+1]=='1':
            cnt +=1
            break
        elif n[j]== 'O' and n[j+1]=='I':
            cnt +=1
            break
print(cnt)