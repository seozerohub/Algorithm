box = 1
cnt = 1
num = int(input())
while num > box:
    box = box + cnt*6 
    cnt = cnt + 1 
print(cnt)