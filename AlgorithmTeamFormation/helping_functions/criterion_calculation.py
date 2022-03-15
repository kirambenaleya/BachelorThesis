from statistics import mean

from AlgorithmTeamFormation.helping_functions.calculate_euclidean_distance import calculate_euclidean_distance


def criterion_calculation(group, student, pt, weights):
    # Set the internal group distance to 0
    igd = 0
    # Initiate the group average distance as an empty list
    gad = []

    # Iterate over the group
    for member in group:
        # Calculate the weighted euclidean distance
        ed = calculate_euclidean_distance(student[1], member[1], weights)
        # Check if this value is the same or larger than the pairwise threshold
        if pt <= ed:
            # If this is the case add the euclidean distance to the internal group distance
            igd += ed
            # Append the euclidean distance to the gad array
            gad.append(ed)
        else:
            # If this is not the case, set both values to -1 and return.
            igd = -1
            gad = -1
            return igd, gad
    # Make sure idg is larger than 0.
    assert igd >= 0

    # Calculate the final group average distance by taking the mean of all values.
    gad = mean(gad)
    return igd, gad
