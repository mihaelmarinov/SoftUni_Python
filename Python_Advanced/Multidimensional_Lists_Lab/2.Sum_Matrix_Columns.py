(rows, columns) = map(int, input().split(','))

matrix = []
for row_index in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

index = 0

for c in range(columns):
    result = 0
    for r in range(rows):
        result += matrix[r][index]
    index += 1
    print(result)
