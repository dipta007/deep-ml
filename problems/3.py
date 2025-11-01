import numpy as np


def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
    try:
        arr = np.array(a)
        arr = arr.reshape(new_shape)
        arr = arr.tolist()
        return arr
    except Exception as e:
        return []


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    new_shape = (3, 2)
    print(reshape_matrix(a, new_shape))
