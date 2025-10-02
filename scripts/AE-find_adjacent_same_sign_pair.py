def find_adjacent_same_sign_pair(numbers):
    for i in range(len(numbers) - 1):
        current_num = numbers[i]
        next_num = numbers[i+1]

        if (current_num > 0 and next_num > 0) or (current_num < 0 and next_num < 0) or (current_num == 0 and next_num == 0):
            return (current_num, next_num)
    return None

input_line = input()

numbers = list(map(int, input_line.split()))

result_pair = find_adjacent_same_sign_pair(numbers)

if result_pair:
    print(result_pair[0], result_pair[1])
