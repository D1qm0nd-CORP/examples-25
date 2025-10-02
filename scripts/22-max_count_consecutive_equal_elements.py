def max_count_consecutive_equal_elements():
    max_length = 0
    current_length = 0
    previous_number = None
    while True:
        number = int(input())
        if number == 0:
            break

        if previous_number is None:
            current_length = 1
        elif number == previous_number:
            current_length += 1
        else:
            current_length = 1

        # Обновляем максимальную длину, если текущая больше
        if current_length > max_length:
            max_length = current_length

        previous_number = number

    print(max_length)

max_count_consecutive_equal_elements()