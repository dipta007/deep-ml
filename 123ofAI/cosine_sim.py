import numpy as np


def cosine_similarity_loss(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    up = x * y
    up = np.sum(up, axis=1)
    # print(up, np.sqrt(x), np.max(np.sqrt(x), np.ones_like(x)))
    norm_x = np.linalg.norm(x, axis=1)
    norm_y = np.linalg.norm(y, axis=1)
    denom = norm_x * norm_y
    cosine = np.zeros_like(up)
    valid = denom != 0

    cosine[valid] = up[valid] / denom[valid]
    loss = 1 - cosine
    res = np.round(np.mean(loss), 4)
    return res


if __name__ == "__main__":
    # list of shape n,d
    # [[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [1.0, 0.0]]
    x = [[1, 0], [0, 1]]
    y = [[1, 0], [1, 0]]
    print(cosine_similarity_loss(x, y))

    x = [[0.0, 0.0]]
    y = [[1.0, 1.0]]
    print(cosine_similarity_loss(x, y))

    # [[3, 4], [5, 12]], [[3, 4], [0, 1]]
    x = [[3, 4], [5, 12]]
    y = [[3, 4], [0, 1]]
    print(cosine_similarity_loss(x, y))
