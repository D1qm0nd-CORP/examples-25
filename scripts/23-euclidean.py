# TODO: FIX 3/23

def euclidean(a, b):
    steps = 0
    while b != 0:
        remainder = a % b  
        a = b  
        b = remainder  
        steps += 1  
    return a, steps  


# Получаем входные данные от пользователя
input_str = input()
num1_str, num2_str = input_str.split()
num1 = int(num1_str)
num2 = int(num2_str)

nod, num_steps = euclidean(num1, num2)
print(f"{nod} {num_steps}")
