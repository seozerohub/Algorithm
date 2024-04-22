white_paper = [[0]*100 for _ in range(100)]
count = 0
a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            white_paper[j][k] += 1

for i in range(100):
    for j in range(100):
        if white_paper[i][j] == 0:
            count +=1

print(100*100 - count)