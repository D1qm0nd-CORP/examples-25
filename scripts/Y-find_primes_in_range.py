def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(a, b):
    prime_numbers = []
    for num in range(a, b + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

a, b = map(int, input().split())

primes = find_primes_in_range(a, b)

if primes:
    print(*primes)  # Распаковка списка для вывода через пробел
else:
    print(0)
