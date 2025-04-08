import math
def solution(n1, d1, n2, d2):
    a = d1*d2 // (math.gcd(d1,d2)) #최소 공배수
    r = (a//d1)*n1 + (a//d2)*n2
    if math.gcd(r,a) != 1:
        result = [r//math.gcd(r,a), a//math.gcd(r,a)]
    else:
        result = [(a//d1)*n1 + (a//d2)*n2, a]
    return result