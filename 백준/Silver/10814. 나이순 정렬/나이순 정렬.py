a = int(input())
idlist = []
for i in range(a):
    age, name = input().split()
    id = [int(age), name, i]
    idlist.append(id)

idlist.sort(key= lambda x: (x[0],x[2]))

for i in idlist:
    for j in range(1):
        print(i[0],i[1])