"""
https://www.deep-ml.com/problems/2
"""


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    ret = []
    r, c = len(a), len(a[0])
    for i in range(c):
        curr = []
        for j in range(r):
            curr.append(a[j][i])
        ret.append(curr)
    return ret


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(a))
