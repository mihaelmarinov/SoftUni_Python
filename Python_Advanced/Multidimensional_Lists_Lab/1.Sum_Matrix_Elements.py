def read_matrix():
    (rows, columns) = map(int, input().split(','))

    matrix = []
    for row_index in range(rows):
        row = list(map(int, input().split(',')))
        matrix.append(row)

    return matrix


matrix = read_matrix()
result = 0

for r in range(len(matrix)):
    result += sum(matrix[r])


print(result)
print(matrix)