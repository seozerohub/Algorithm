a = int(input())
for i in range(1,a):
    print(" "*(i-1)+"*"*(2*a-2*i+1))

for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))