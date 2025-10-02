def is_power_of_two(n):
    if n <= 0:
        return False
    
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2  

    return True

n = int(input())

if is_power_of_two(n):
    print("YES")
else:
    print("NO")