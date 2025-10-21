def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    r, c = len(matrix), len(matrix[0])
    result = []
    for i in range(r):
        curr = []
        for j in range(c):
            curr.append(matrix[i][j] * scalar)
        result.append(curr)

    return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    scalar = 2
    print(scalar_multiply(matrix, scalar))
