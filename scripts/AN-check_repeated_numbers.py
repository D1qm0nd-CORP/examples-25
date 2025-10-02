def check_repeated_numbers():
    line = input() 
    numbers = line.split() 
    seen_numbers = set()  

    for number in numbers:
        if number in seen_numbers:
            print("YES")
        else:
            print("NO")
            seen_numbers.add(number) 

check_repeated_numbers()
