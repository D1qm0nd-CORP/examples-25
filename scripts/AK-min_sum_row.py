def find_min_sum_row(matrix):
    min_sum = float('inf')  
    min_row_index = -1

    for i, row in enumerate(matrix):
        current_sum = sum(row)
        if current_sum < min_sum:
            min_sum = current_sum
            min_row_index = i

    return matrix[min_row_index]

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_sum_row = find_min_sum_row(matrix)

print(" ".join(map(str,min_sum_row)))
