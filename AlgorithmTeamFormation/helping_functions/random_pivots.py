import random
import warnings


def random_pivots(tuples_students, number_of_groups):
    # Ignore the warning output
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Randomly select the initial pivots
    initial_pivots = random.sample(tuples_students, k=number_of_groups)
    # Initialize an empty list of pivots
    pivots = []
    # Set the leftover students to all students
    leftoverStudents = tuples_students

    # Iterate through the pivots and append them to the pivot list.
    for pivot in initial_pivots:
        pivots.append(pivot)

        # Iterate through the list of leftover students and remove the pivots based on their matriculation number
        for student in leftoverStudents:
            if pivot[0] in student:
                leftoverStudents.remove(student)

    # Return both lists
    return pivots, leftoverStudents
