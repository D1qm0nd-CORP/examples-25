def find_max_element():
    max_element = -1  # Инициализируем максимальный элемент отрицательным значением, так как числа натуральные (больше 0)
    while True:
        num = int(input())
        if num == 0:  # Если встретили 0, это конец последовательности
            break
        if num > max_element:  # Если текущее число больше текущего максимума
            max_element = num  # Обновляем максимум
    print(max_element)

find_max_element()