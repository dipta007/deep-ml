import numpy as np


def confusion_matrix(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    # Your code here
    TN = sum((y_true == 0) & (y_true == y_pred))
    TP = sum((y_true == 1) & (y_true == y_pred))
    FP = sum((y_true == 0) & (y_pred == 1))
    FN = sum((y_true == 1) & (y_pred == 0))

    return np.asarray([[TN, FP], [FN, TP]])


if __name__ == "__main__":
    y_true = [0, 0, 1, 1]
    y_pred = [0, 1, 0, 1]
    print(confusion_matrix(y_true, y_pred))
