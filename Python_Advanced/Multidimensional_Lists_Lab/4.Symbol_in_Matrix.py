row_column = int(input())

matrix = []

for i in range(row_column):
    row = list(input())
    matrix.append(row)

symbol = input()
symbol_in = False
location = []

for row in range(row_column):
    if symbol_in:
        break
    for column in range(row_column):
        if matrix[row][column] == symbol:
            location = [row, column]
            symbol_in = True

if symbol_in:
    print(f'({location[0]}, {location[1]})')
else:
    print(f"{symbol} does not occur in the matrix")
