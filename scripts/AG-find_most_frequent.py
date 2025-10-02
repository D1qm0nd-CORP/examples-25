def find_most_frequent(numbers):
    max_count = 0
    most_frequent_number = None

    for number in numbers:
        current_count = 0
        for other_number in numbers:
            if number == other_number:
                current_count += 1

        if current_count > max_count:
            max_count = current_count
            most_frequent_number = number

    return most_frequent_number

input_str = input()
numbers_list = list(map(int, input_str.split()))

result = find_most_frequent(numbers_list)
print(result)
