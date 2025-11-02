def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    def cov(x, y, mnx, mny):
        m = len(x)
        res = 0
        for _x, _y in zip(x, y):
            res += (_x - mnx) * (_y - mny)
        res = res / (m - 1)
        return res

    l = len(vectors)
    res = [[1.0 for _ in range(l)] for __ in range(l)]
    mean = [sum(v) / len(v) for v in vectors]
    for i in range(l):
        for j in range(l):
            res[i][j] = cov(vectors[i], vectors[j], mean[i], mean[j])
    return res


if __name__ == "__main__":
    vectors = [[1, 2, 3], [4, 5, 6]]
    print(calculate_covariance_matrix(vectors))
