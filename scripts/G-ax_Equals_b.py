#TODO: FIX 7/9

def solve_linear_equation_integers(a, b):
    if a == 0:
        if b == 0:
            return "many solutions"
        else:
            return "no solution"
    else:
        if b % a == 0:
            x = b // a 
            return x
        else:
            return "no solution"

def check(value):
    if abs(value) > 30000:
        return False
    return True

def Input():
    val = input().split(' ')
    return int(val[0]), int(val[1])

a, b  = Input()

if check(a) and check(b):
    print(solve_linear_equation_integers(a, b))  # Ожидаемый вывод: Единственное решение: x = 5
else:
    raise Exception("arguments are not correct")
