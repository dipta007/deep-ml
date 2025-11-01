def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    r, c = len(matrix), len(matrix[0])
    if mode == "row":
        rows = []
        for i in range(r):
            cum = 0
            for j in range(c):
                cum += matrix[i][j]
            rows.append(cum / c)
        return rows
    else:
        cols = []
        for i in range(c):
            cum = 0
            for j in range(r):
                cum += matrix[j][i]
            cols.append(cum / r)
        return cols


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    mode = "row"
    print(calculate_matrix_mean(matrix, mode))
    mode = "column"
    print(calculate_matrix_mean(matrix, mode))
