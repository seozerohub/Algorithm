
import sys
input = sys.stdin.readline
a = int(input())
cnt = [0]*(10001)

for i in range(a):
    n = int(input())
    cnt[n] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)