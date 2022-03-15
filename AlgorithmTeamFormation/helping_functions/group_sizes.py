from math import ceil


def determine_group_sizes(students, max_number_students_per_group):
    # Make sure the values are chosen correctly and make sense
    assert isinstance(students, int)
    assert isinstance(max_number_students_per_group, int)
    assert students > 0
    assert max_number_students_per_group > 0

    # Calculate the number of groups
    groups = ceil(students / max_number_students_per_group)
    sizes = []

    # While the number of students is larger than 0 keep calculating the amount of group members per group
    while students > 0:
        number = ceil(students / groups)
        sizes.append(number)
        students = students - number
        groups = groups - 1

    # Return the list of group sizes
    return sizes
