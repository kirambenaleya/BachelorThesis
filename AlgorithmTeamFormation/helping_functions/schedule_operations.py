import numpy as np


def compare_schedule(schedule1, schedule2):
    # Make sure both arrays have the same shape
    assert schedule1.shape == schedule2.shape

    # Multiply both matrices/arrays elementwise to receive a single matrix/array that contains the shared schedule
    return np.multiply(schedule1, schedule2)


def same_availability(student1, student2):
    if not student1 or not student2:
        return 0
    # Determine the shared schedule
    schedule = compare_schedule(student1[1][6:], student2[1][6:])
    # Return the number of shared elements, indication when both students have time
    return np.count_nonzero(schedule)
