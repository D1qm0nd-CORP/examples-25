def check_same_digits(number_str):
    if not number_str:
        return 'NO' 

    first_digit = number_str[0]
    for digit in number_str:
        if digit != first_digit:
            return 'NO'
    return 'YES'

input_number_str = input()

print(check_same_digits(input_number_str))