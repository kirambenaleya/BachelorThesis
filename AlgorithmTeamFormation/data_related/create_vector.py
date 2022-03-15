import numpy as np


def create_vector(students):
    # Check if students is empty
    if not students or len(students) < 1:
        return None

    # Check that students is a list
    assert isinstance(students, list)

    # Loop through the list of students
    for student in students:
        # Check that each element of the list is a dictionary
        assert isinstance(student, dict)

        # Initiate a empty list to append all keys
        dict_keys = []

        # Loop through the key(s) and extract the key(s)
        for key in student.keys():
            dict_keys.append(key)

        # Extract the matriculation number
        key = dict_keys[0]

        # Make sure the variable key exists and was assigned correctly
        assert len(key) != 0

        # Create the student vector
        student[key]['vector'] = [student[key]['Gender'], student[key]['Experience'], student[key]['Education Level'],
                                  student[key]['Major'], student[key]['Attempt'], student[key]['Teammate']]

        student[key]['vector'].extend(student[key]['Schedule'])
        # Check if the vector has the right length
        assert len(student[key]['vector']) == 27

        # Transform the list into a numpy array to make calculations more efficient
        student[key]['vector'] = np.array(student[key]['vector'])

        # Normalize the vector
        # student[key]['vector'] = student[key]['vector'] / np.sqrt(np.sum(student[key]['vector']**2))

    # Return the list
    return students
