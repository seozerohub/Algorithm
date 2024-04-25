from decimal import Decimal

coin = []
a = int(input())
for i in range(a):
    c = Decimal(input())
    c = c * Decimal('0.01')

    qu = c // Decimal('0.25')
    c = c - qu * Decimal('0.25')
    coin.append(qu)
    da = c // Decimal('0.10')
    c = c - da * Decimal('0.10')
    coin.append(da)
    ni = c // Decimal('0.05')
    c = c - ni * Decimal('0.05')
    coin.append(ni)
    pa = c // Decimal('0.01')
    coin.append(pa)

    for j in coin:
        print(int(j), end=' ')
    coin = []