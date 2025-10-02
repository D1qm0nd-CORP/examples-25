def find_saddle_points(n, m, matrix):
    saddle_points = []
    row_min_indices = [0] * n
    for r in range(n):
        min_val = matrix[r][0]
        min_idx = 0
        for c in range(1, m):
            if matrix[r][c] < min_val:
                min_val = matrix[r][c]
                min_idx = c
        row_min_indices[r] = min_idx

    for r in range(n):
        potential_c = row_min_indices[r]
        current_value = matrix[r][potential_c]

        is_max_in_column = True
        for row_check in range(n):
            if matrix[row_check][potential_c] > current_value:
                is_max_in_column = False
                break

        if is_max_in_column:
            saddle_points.append((r + 1, potential_c + 1))

    if not saddle_points:
        return 0
    else:
        return saddle_points



n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = find_saddle_points(n, m, matrix)

if result == 0:
    print(0)
else:
    for point in result:
        print(point[0], point[1])

