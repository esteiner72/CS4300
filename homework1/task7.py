import numpy as np

def task7_1():
    # We will be multiplying two 2x2 matrices together and taking the determinant of the product
    a = ([2, 1],
        [1, 2])
    b = ([3, 1],
        [2, 1])

    product = np.matmul(b, a)

    return round(np.linalg.det(product))
