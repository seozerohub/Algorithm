cnt = 2
a = int(input())
for i in range(a):
    cnt = cnt + (cnt-1)

j = cnt**2
print(j)