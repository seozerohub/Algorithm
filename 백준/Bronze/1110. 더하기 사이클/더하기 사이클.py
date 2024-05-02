num = input()
n = list(num)
t =[]
cnt =0

if int(num)<10:
    t.append(0)
    t.append(int(num))
else:
    for i in n:
        i = int(i)
        t.append(i)

while True:
    r = t[0] + t[1]
    if r <10:
        k = t[1]
        cnt = cnt + 1
        t = []
        t.append(k)
        t.append(r)
    else:
        r = list(str(r))
        k = t[1]
        cnt = cnt + 1
        t = []
        t.append(k)
        t.append(int(r[1]))
    if int(num) == t[0] * 10 + t[1]:
        break
        
print(cnt)