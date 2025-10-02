def count_even_digits(number_str):
    even_count = 0
    for digit in number_str:
        if int(digit) % 2 == 0:
            even_count += 1
    return even_count

input_number_str = input()

result = count_even_digits(input_number_str)
print(result)