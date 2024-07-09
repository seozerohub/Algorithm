alist  = []
for i in range(5):
    a = int(input())
    alist.append(a)
x = min(alist[:3])
y = min(alist[3:])
print(x+y-50)