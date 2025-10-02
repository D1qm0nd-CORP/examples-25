input_line = input()

numbers = list(map(int, input_line.split()))

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

if odd_numbers:
    print(min(odd_numbers))
else:
    print(0)
