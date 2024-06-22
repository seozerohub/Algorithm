num = 0
num1 = 0
num2 = 0
for i in range(15):
    a = list(input())
    for j in a:
        if j == 'w':
            num +=1
        elif j=='b':
            num1 +=1
        elif j=='g':
            num2 +=1

if num !=0:
    print("chunbae")
elif num1 !=0:
    print("nabi")
elif num2 !=0:
    print("yeongcheol")