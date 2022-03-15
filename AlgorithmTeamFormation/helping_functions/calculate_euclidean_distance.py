from numpy import sqrt


def calculate_euclidean_distance(x, y, weights):
    sum_weights = 0
    for element in weights:
        assert element >= 0
        sum_weights += element

    assert abs(1 - sum_weights) < 0.0001
    assert sum_weights > 0

    # Only consider the attributes that should be heterogeneous
    x = x[0:5]
    y = y[0:5]

    # Calculate the difference
    q = x - y
    # Return the square root of the squared value of sum * weights
    return sqrt((weights * q * q).sum())
