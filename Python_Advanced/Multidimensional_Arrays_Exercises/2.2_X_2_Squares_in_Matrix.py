(rows, columns) = map(int, input().split(','))

matrix = []
for row_index in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)



def equal_counter(matrix):
    equal = 0

    for r in range(rows):
        two_equal = 0
        current_symbol = 
        for c in range(columns):
            if matrix[r][c]