def isEvenHasOdd(num, hasEven, hasOdd):
    if a % 2 == 0:
        has_even = True
    else:
        has_odd = True


def check_even_odd_mix(a, b, c):
    has_even = False
    has_odd = False
    if a % 2 == 0:
        has_even = True
    else:
        has_odd = True

    if b % 2 == 0:
        has_even = True
    else:
        has_odd = True
    if c % 2 == 0:
        has_even = True
    else:
        has_odd = True
    
    if has_even and has_odd:
        return "YES"
    else:
        return "NO"

a = int(input())
b = int(input())
c = int(input())

print(check_even_odd_mix(a, b, c))
