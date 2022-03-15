from AlgorithmTeamFormation.helping_functions.criterion_calculation import criterion_calculation
from AlgorithmTeamFormation.helping_functions.schedule_operations import same_availability


def find_fitting_student(leftover_students, group_configuration, index, pt, gt, weights, sizes, schedules):
    # Initiate the list that contains all students that can potentially be added to a team
    possible_students = []

    # This variable determines how many schedule-matches students must have to be considered.
    # TODO: Decide on which value to use
    same_time_available = 5

    iteration = 0

    # Make sure no empty groups have been passed
    for group in group_configuration:
        assert len(group) >= 1

    while sizes[index] > len(group_configuration[index]) and iteration < 5:
        # Define the previously added student
        student = group_configuration[index][-1]

        # CASE 1: Previously added student has no teammate.
        if student[1][5] == 0:
            # Create a minority listing
            possible_students = [person for person in leftover_students if (person[1][0] != student[1][0] or person[1][2]
                                                                            != student[1][2] or person[1][3] !=
                                                                            student[1][3] or person[1][4] != student[1][
                                                                              4]) and
                                 same_availability(student, person) >= same_time_available]

        # CASE 2: Previously added student has a teammate.
        elif student[1][5] != 0:
            # Determine if the teammate is still available and if this is the case add them to the list.
            possible_students = [person for person in leftover_students if person[1][5] == student[1][5] and
                                 same_availability(student, person) >= same_time_available]

        # CASE 3: No matches were found because one or more criteria have not been met. In this case check the schedule.
        if not possible_students:
            possible_students = [person for person in leftover_students if same_availability(student, person) >=
                                 same_time_available]

        # CASE 4: No matching schedules were determined. In this case just choose students at random.
        if not possible_students:
            possible_students = leftover_students

        # Iterate through the list of possible students and try to fill the group with students that match the
        # criteria fitting pt and gt conditions.
        for std in possible_students:
            # Calculate the internal group distance and the group average distance
            igd, gad = criterion_calculation(group_configuration[index], std, pt, weights)

            # Check if the criteria are met
            if gad != -1 and igd >= gt:
                # Add the student to the group
                group_configuration[index].append(std)
                #schedules[index].append(compare_schedule(schedules[index], std[6:0]))
                # Remove the student from the pool of leftover students
                leftover_students.remove(std)

                # Check if the group is full
                if sizes[index] == len(group_configuration[index]):
                    # Add the calculated data if the group is full
                    data = {"igd": igd, "gad": gad}
                    group_configuration[index].append(data)
                    # Break to be more efficient and cut off the for loop
                    break

        # Increase the value of iteration by 1
        iteration += 1

    # Return the new group configuration
    return group_configuration, schedules
