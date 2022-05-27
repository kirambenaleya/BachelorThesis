# import libraries
from numpy import *
import random

from AlgorithmTeamFormation.data_related.create_tuple import convert_to_tuples
from AlgorithmTeamFormation.data_related.create_vector import create_vector
from AlgorithmTeamFormation.data_related.preprocess_data import preprocess_data
from AlgorithmTeamFormation.enums.attempt import Attempt
from AlgorithmTeamFormation.helping_functions.case_2_criterion_calculation import criterion_calculation_case_2
from AlgorithmTeamFormation.helping_functions.find_matching_student import find_fitting_student
from AlgorithmTeamFormation.helping_functions.group_sizes import determine_group_sizes
from AlgorithmTeamFormation.helping_functions.skilled_pivots import skilled_pivots
from AlgorithmTeamFormation.optimize.swap_best_worst import *


def team_formation_algorithm(delimiter, maximum_per_group, student_data, weights=None):
    if weights is None:
        # TODO: Determine weights based on ranking made by students of prior year
        weights = [0.4, 0.3, 0.1, 0.1, 0.1]

    # Import and clean up data
    students = preprocess_data(student_data, delimiter)

    # Create the vector used for the distance calculations
    students = create_vector(students)

    number_of_students = len(students)
    # Calculate the number of groups
    sizes = determine_group_sizes(len(students), maximum_per_group)
    number_of_groups = len(sizes)

    # Set formula
    random_allocation_threshold = 0.2
    step_size = 0.025

    # The lower limit for a heterogeneous grouping
    pt = 0.3

    attempt = Attempt.first
    satisfied = False
    # Iterate through the students that haven't been allocated to a group yet
    while not satisfied:
        if attempt.first or attempt.second:
            # Extract matriculation ID and the vector and create a list of tuples
            tuples_students = convert_to_tuples(students)
            # Select random pivots (in second iteration we can specify different methods of selecting the pivots)
            pivots, leftover_students = skilled_pivots(tuples_students, number_of_groups)
            group_configuration = []
            schedules = []
            # Allocate each pivot as first group member
            for pivot in pivots:
                group_configuration.append([pivot])
                schedules.append([pivot[6:]])

        assert leftover_students and pivots and group_configuration and schedules
        assert len(pivots) == len(group_configuration)
        assert len(leftover_students) == number_of_students - len(group_configuration)

        for index, pivot in enumerate(group_configuration):
            # Iterate through the list of pivots and compare the vector of the student chosen as a pivot with potential
            # candidates until a match is found, then continue

            if sizes[index] > len(group_configuration[index]):
                # Number of initial group members (will be == 1 once all pivots have been chosen)
                m = len(group_configuration[index])
                # This value is calculated based on the number of group members m. This is the upper limit for internal
                # group distance in the case of homogeneous grouping and lower limit in case of heterogeneous grouping
                gt = pt * (m - 1)

                find_fitting_student(leftover_students, group_configuration, index, pt, gt, weights, sizes, schedules)

        attempt = Attempt(attempt.value + 1)

        if not leftover_students:
            print("CASE 1")
            satisfied = True

        elif leftover_students and len(leftover_students) <= random_allocation_threshold * number_of_students:
            print("CASE 2")

            for index, group in enumerate(group_configuration):
                while sizes[index] > len(group_configuration[index]):
                    student = random.choice(leftover_students)
                    igd, gad = criterion_calculation_case_2(group_configuration[index], student, weights)
                    group_configuration[index].append(student)
                    leftover_students.remove(student)
                    if sizes[index] == len(group_configuration[index]):
                        data = {"igd": igd, "gad": gad}
                        group_configuration[index].append(data)

            satisfied = True

        elif not all(len(group_configuration) >= 3) and attempt.second:
            print("CASE 3")
            pt -= step_size

        else:
            print("CASE 4")
            pt -= step_size
            attempt = attempt.first

    dictionary = {}

    for index, group in enumerate(group_configuration):
        key_index = str(index + 1)
        dictionary_key = str("Group " + key_index)
        dictionary[dictionary_key] = []
        for index2, member in enumerate(group):
            if member != group[-1]:
                key_index = str(index2 + 1)
                new_dictionary_key = str("Team member " + key_index)
                group_member = {new_dictionary_key: member[0]}
                dictionary[dictionary_key].append(group_member)
            else:
                data = {'Data': member}
                dictionary[dictionary_key].append(data)
    return dictionary
