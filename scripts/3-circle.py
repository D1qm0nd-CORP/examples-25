import math

radius = float(input())
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print(f'{area:.3f}')
print(f"{circumference:.3f}")