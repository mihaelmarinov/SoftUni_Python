(rows, columns) = map(int, input().split())

matrix = []
submatrix_size = 3
for r in range(rows):
    matrix.append(list(map(int, input().split())))


def sum_submatrix(matrix, row_i, cow_i, size):
    submatrix_sum = 0
    for r in range(row_i, row_i + size):
        for c in range(cow_i, cow_i + size):
            submatrix_sum += matrix[r][c]

    return submatrix_sum


def best_submatrix(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_result = sum_submatrix(matrix, 0, 0, submatrix_size)

    for row in range(len(matrix) - submatrix_size + 1):
        for col in range(len(matrix[row]) - submatrix_size + 1):
            current_sum = sum_submatrix(matrix, row, col, submatrix_size)
            if best_result < current_sum:
                best_result = current_sum
                best_column_index = col
                best_row_index = row
    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates

    print(f'Sum = {sum_submatrix(matrix, row_index,col_index, size)}')
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(el) for el in row))


print_result(best_submatrix(matrix,submatrix_size), submatrix_size)