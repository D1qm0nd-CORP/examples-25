def count_max_elements():
    max_element = -100000000000000
    count = 0

    while True:
        num = int(input())

        if num == 0:
            break

        if num > max_element:
            max_element = num
            count = 1
        elif num == max_element:
            count += 1

    if max_element == -100000000000000:
        print("Последовательность пуста.")
    else:
        print(count)

count_max_elements()
