import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    mean_columns = np.mean(matrix, axis=0).tolist()
    mean_rows = np.mean(matrix, axis=1).tolist()
    mean_all = np.mean(matrix).tolist()

    variance_columns = np.var(matrix, axis=0).tolist()
    variance_rows = np.var(matrix, axis=1).tolist()
    variance_all = np.var(matrix).tolist()

    std_columns = np.std(matrix, axis=0).tolist()
    std_rows = np.std(matrix, axis=1).tolist()
    std_all = np.std(matrix).tolist()

    max_columns = np.max(matrix, axis=0).tolist()
    max_rows = np.max(matrix, axis=1).tolist()
    max_all = np.max(matrix).tolist()

    min_columns = np.min(matrix, axis=0).tolist()
    min_rows = np.min(matrix, axis=1).tolist()
    min_all = np.min(matrix).tolist()

    sum_columns = np.sum(matrix, axis=0).tolist()
    sum_rows = np.sum(matrix, axis=1).tolist()
    sum_all = np.sum(matrix).tolist()

    return {
        "mean": [mean_columns, mean_rows, mean_all],
        "variance": [variance_columns, variance_rows, variance_all],
        "standard deviation": [std_columns, std_rows, std_all],
        "max": [max_columns, max_rows, max_all],
        "min": [min_columns, min_rows, min_all],
        "sum": [sum_columns, sum_rows, sum_all]
    }
