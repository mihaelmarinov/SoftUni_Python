def read_matrix():
    (rows, columns) = map(int, input().split(','))

    matrix = []
    for row_index in range(rows):
        row = list(map(int, input().split(',')))
        matrix.append(row)

    return matrix


def sum_submatrix(matrix, row_i, cow_i, size):
    submatrix_sum = 0
    for r in range(row_i, row_i + size):
        for c in range(cow_i, cow_i + size):
            submatrix_sum += matrix[r][c]

    return submatrix_sum


def print_result(coordinates, size):
    (row_index, col_index) = coordinates

    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(el) for el in row))
    print(sum_submatrix(matrix, row_index,col_index, size))


def best_submatrix(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_result = sum_submatrix(matrix, 0, 0, submatric_size)

    for row in range(len(matrix) - submatric_size + 1):
        for col in range(len(matrix[row]) - submatric_size + 1):
            current_sum = sum_submatrix(matrix, row, col, submatric_size)
            if best_result < current_sum:
                best_result = current_sum
                best_column_index = col
                best_row_index = row
    return (best_row_index, best_column_index)


matrix = read_matrix()
submatric_size = 2

print_result(best_submatrix(matrix,submatric_size), submatric_size)


