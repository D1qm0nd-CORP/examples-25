import math
def RunScript():
    a, b  = InputValues()
    print(MathGipothenuse(a, b))

def MathGipothenuse(a, b):
    return math.sqrt(a**2+b**2)
def InputValues():
    a = float(input())
    b = float(input())
    return a,b

RunScript()