def find_perfect_squares(N):
    i = 1
    while True:
        square = i * i  
        if square <= N:
            print(square)
            i += 1
        else:
            break 

n = int(input())
find_perfect_squares(n)