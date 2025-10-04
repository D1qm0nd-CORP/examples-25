def find_adjacent_same_sign_pair(numbers_str):
    numbers = list(map(int, numbers_str.split())) 

    for i in range(len(numbers) - 1):
        current_num = numbers[i]
        next_num = numbers[i+1]

        if (current_num > 0 and next_num > 0) or (current_num < 0 and next_num < 0):
            return f"{current_num} {next_num}"  

    return None 

input_line = input()
result = find_adjacent_same_sign_pair(input_line)

if result:
    print(result)