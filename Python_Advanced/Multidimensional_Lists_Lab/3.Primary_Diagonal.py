row_column = int(input())

matrix = []

for i in range(row_column):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_prime_diagonal = 0
index = 0

for sq in range(row_column):
    sum_prime_diagonal += matrix[sq][index]
    index += 1

print(sum_prime_diagonal)