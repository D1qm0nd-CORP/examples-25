def find_smallest_divisor(n):
    for i in range(2, n + 1):  
        if n % i == 0: 
            return i  

n = int(input())
result = find_smallest_divisor(n)
print(result)