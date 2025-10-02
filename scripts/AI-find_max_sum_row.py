def find_max_sum_row(n, m, matrix):
    max_sum = -1  
    max_row_index = -1

    for i in range(n):
        current_sum = 0
        for j in range(m):
            current_sum += matrix[i][j]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = i

    return max_sum, max_row_index

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result_sum, result_index = find_max_sum_row(n, m, matrix)

print(f"{result_sum}\n{result_index}")

