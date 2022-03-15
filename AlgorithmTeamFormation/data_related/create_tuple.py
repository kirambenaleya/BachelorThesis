def convert_to_tuples(students):
    if not students:
        return None
    # Initiate an empty list to add the student tuples to
    list_of_tuples = []

    # Loop through all students
    for student in students:
        # Extract each key
        first_key = []

        for key in student.keys():
            # Extract the matriculation number
            first_key.append(key)

        # Create a new tuple containing the matriculation number and the vector of each student. Using tuples ensures
        # that the values are immutable and not changed from here on out.
        new_tuple = (first_key[0], student[first_key[0]]["vector"])
        # Add the tuple to the list
        list_of_tuples.append(new_tuple)

    # Return the list
    return list_of_tuples
