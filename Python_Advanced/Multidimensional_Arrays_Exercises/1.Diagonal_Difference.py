size = int(input())
matrix_r = []

for row in range(size):
    matrix_r.append(list(map(int, input().split())))


def primary_diagonal(matrix):
    prime_sum = 0
    index = 0
    for r in range(len(matrix)):
        prime_sum += matrix[r][index]
        index += 1

    return prime_sum


def secondary_diagonal(matrix):
    secondary_sum = 0
    index = 0
    for r in range(len(matrix)-1, -1, -1):
        secondary_sum += matrix[r][index]
        index += 1

    return secondary_sum


def prime_secondary_difference(prime, secondary):
    result = abs(prime - secondary)

    print(result)


prime_secondary_difference(primary_diagonal(matrix_r), secondary_diagonal(matrix_r))