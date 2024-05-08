import sys
input = sys.stdin.readline

a = int(input())
cnt = [0]*2000001
offset = 1000000

for i in range(a):
    n = int(input()) + offset
    cnt[n] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i - offset)