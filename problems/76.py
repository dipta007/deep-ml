import numpy as np


def cosine_similarity(v1, v2):
    # Implement your code here
    up = np.dot(v1, v2)
    v1_ = np.dot(v1, v1)
    v2_ = np.dot(v2, v2)
    return round(up / (np.sqrt(v1_) * np.sqrt(v2_)), 3)


if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print(cosine_similarity(v1, v2))
