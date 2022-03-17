# import libraries
import pandas as pd

from AlgorithmTeamFormation.enums.attempt import Attempt
from AlgorithmTeamFormation.enums.bachelor import Bachelor
from AlgorithmTeamFormation.enums.experience import Experience
from AlgorithmTeamFormation.enums.gender import Gender
from AlgorithmTeamFormation.enums.major import Major


def preprocess_data(filepath, delimiter):
    # Read in data
    try:
        data = pd.read_csv(filepath, delimiter=delimiter)
    except pd.errors.EmptyDataError:
        print("File is empty or can not be read.")
        return None

    # Initialize empty list
    students = []

    # Preprocess data and convert all strings to ints to allow for calculation in later steps
    print(data)
    data.loc[data['Bachelor/Master'] == 'bachelor', 'Bachelor/Master'] = Bachelor.bachelor.value
    data.loc[data['Bachelor/Master'] == 'master', 'Bachelor/Master'] = Bachelor.master.value
    data.loc[data['Major/Minor'] == 'major', 'Major/Minor'] = Major.major.value
    data.loc[data['Major/Minor'] == 'minor', 'Major/Minor'] = Major.minor.value
    data.loc[data['Gender'] == 'male', 'Gender'] = Gender.male.value
    data.loc[data['Gender'] == 'female', 'Gender'] = Gender.female.value
    data.loc[data['Gender'] == 'non binary', 'Gender'] = Gender.nonBinary.value
    data.loc[data['Experience'] == 'no', 'Experience'] = Experience.no.value
    data.loc[data['Experience'] == 'yes', 'Experience'] = Experience.yes.value
    data.loc[data['Attempt'] == 'first', 'Attempt'] = Attempt.first.value
    data.loc[data['Attempt'] == 'second', 'Attempt'] = Attempt.second.value
    # Loop through the data and convert each student to a dictionary
    for index, row in data.iterrows():
        student = {row['Matriculation Number']: {'ID': row['ID'], 'Name': row['First Name'] + " " + row["Last Name"],
                                                 'Gender': row['Gender'], 'Experience': row['Experience'],
                                                 'Education Level': row['Bachelor/Master'], 'Major': row['Major/Minor'],
                                                 'Attempt': row['Attempt'], 'Teammate': row['Teammate'],
                                                 'Schedule': row['Schedule'].strip("'""")}}
        students.append(student)

    # Check if teammates are reciprocal. If this is the case assign them the same team-number otherwise set this
    # value == 0

    # Start with the group number == 1 for the first team
    group_number = 1
    # Loop through each item in the list of students
    for item in students:
        # Retrieve the first (and only) key which is equal to the student matriculation number
        matriculation_key = []
        for key in item.keys():
            matriculation_key.append(key)
        matriculation_key = matriculation_key[0]
        # Check if the key Teammate has a value assigned to it which is different from '0'
        if item[matriculation_key]['Teammate'] != '0' and item[matriculation_key]['Teammate'] != 0:
            # Extract the teammate's matriculation number
            matriculation_number = item[matriculation_key]['Teammate']
            # Loop through the list of all students
            for student in students:
                # Check each entry to see if the key is equal to the matriculation_number
                if student.get(matriculation_number) is not None and student != item:
                    # If the teammates aren't reciprocal set both values to 0
                    if student[matriculation_number]['Teammate'] != matriculation_key:
                        item[matriculation_key]['Teammate'] = 0
                        student[matriculation_number]['Teammate'] = 0
                    # If the teammates are reciprocal set both values to the current group number and increase it by 1
                    else:
                        item[matriculation_key]['Teammate'] = group_number
                        student[matriculation_number]['Teammate'] = group_number
                        group_number += 1
        else:
            # Convert string '0' to int 0 for the vector in the later steps
            item[matriculation_key]['Teammate'] = 0

        # Convert the schedule from a string to a list of int values
        initial_schedule = item[matriculation_key]['Schedule']
        schedule = []
        for character in initial_schedule:
            if character == '+':
                schedule.append(1)
            else:
                schedule.append(0)

        # Confirm that the list has the right length
        assert (len(schedule) == 21)
        item[matriculation_key]['Schedule'] = schedule

        # Confirm that the teammate variable was converted to an int value
        if not isinstance(item[matriculation_key]['Teammate'], int):
            item[matriculation_key]['Teammate'] = 0

    # Return the preprocessed data
    return students
