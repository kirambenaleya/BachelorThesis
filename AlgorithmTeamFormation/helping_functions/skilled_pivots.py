import random
import warnings


def skilled_pivots(tuples_students, number_of_groups):
    # Ignore the warning output
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Filter all students who have prior knowledge
    prior_knowledge = [x for x in tuples_students if x[1][1] == 1]

    if len(prior_knowledge) < number_of_groups:
        missing_number_pivots = number_of_groups - len(prior_knowledge)
        filtered_students = [x for x in tuples_students if x[1][1] != 1]
        prior_knowledge.extend(random.sample(filtered_students, k=missing_number_pivots))

    initial_pivots = random.sample(prior_knowledge, k=number_of_groups)

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
