"""
https://www.deep-ml.com/problems/1?from=Machine%20Learning
"""


def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    r, c = len(a), len(a[0])
    if c != len(b):
        return -1

    ret = []
    for i in range(r):
        curr = 0
        for j in range(c):
            curr += a[i][j] * b[j]
        ret.append(curr)

    return ret


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    b = [1, 2, 3]
    print(matrix_dot_vector(a, b))
