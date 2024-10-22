def FizzBuzz(a):
    if a%3==0 and a%5==0:
        return "FizzBuzz"
    elif a%3==0 and a%5!=0:
        return "Fizz"
    elif a%3!=0 and a%5==0:
        return "Buzz"
    else:
        return a

blist = []
for i in range(3):
    x = input()
    blist.append(x)

r = 3

for i in range(3):
    if blist[i] not in ['Fizz', 'Buzz', 'FizzBuzz']:
        t = int(blist[i])+r
    r = r-1

print(FizzBuzz(t))