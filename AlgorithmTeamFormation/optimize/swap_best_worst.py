import itertools
from operator import itemgetter

from AlgorithmTeamFormation.helping_functions.calculate_euclidean_distance import calculate_euclidean_distance


def find_highest(groups):
    maximum = 0
    max_index = 0
    for index, group in enumerate(groups):
        if group[-1]['igd'] > maximum:
            maximum = group[-1]['igd']
            max_index = index
    return max_index


def find_lowest(groups):
    minimum = 0
    min_index = 0
    for index, group in enumerate(groups):
        if group[-1]['igd'] < minimum:
            minimum = group[-1]['igd']
            min_index = index
    return min_index


def calculate_igd(group, student, weights):
    # Calculates the internal group distance
    igd = 0
    for member in group:
        ed = calculate_euclidean_distance(student[1], member[1], weights)
        igd += ed
    return igd


def try_swapping_best_worst(group_configuration, index_lowest, index_highest, weights):
    # Compare what happens when you swap two members of the lowest and highest scoring teams (might need to consider
    # schedule). Square the igd values of both teams and calculate the product. This way 6,6 scores higher than 11,
    # 2, making the overall distribution fairer. If two members (that have teammate value 0) can be swapped in order to
    # achieve an overall higher average then swap these two members.
    group1 = group_configuration[index_highest]
    group2 = group_configuration[index_lowest]

    initial_igd = (group1[-1]['igd'] ** 2) * (group2[-1]['igd'] ** 2)
    group1 = group1[:-1]
    group2 = group2[:-1]
    potential_swapping_candidates_group1 = []
    potential_swapping_candidates_group2 = []

    for member in group1:
        if member[1][5] == 0:
            potential_swapping_candidates_group1.append(member)

    for member in group2:
        if member[1][5] == 0:
            potential_swapping_candidates_group2.append(member)

    # If there exist potential candidates for swapping in both groups try swapping them and measure the result
    if potential_swapping_candidates_group1 and potential_swapping_candidates_group2:
        potential_groups1 = []
        potential_groups2 = []

        for candidate in potential_swapping_candidates_group1:
            group = group1[:]
            group.remove(candidate)
            potential_groups1.append(group)

        for candidate in potential_swapping_candidates_group2:
            group = group2[:]
            group.remove(candidate)
            potential_groups2.append(group)

        potential_combinations_group1 = [
            {'igd': calculate_igd(group, student, weights), 'group': group, 'student': student}
            for (student, group) in
            itertools.product(potential_swapping_candidates_group2, potential_groups1)]

        potential_combinations_group2 = [
            {'igd': calculate_igd(group, student, weights), 'group': group, 'student': student}
            for (student, group) in
            itertools.product(potential_swapping_candidates_group1, potential_groups2)]

        for entry in potential_combinations_group1:
            entry['group'].append(entry['student'])
            del entry['student']

        for entry in potential_combinations_group2:
            entry['group'].append(entry['student'])
            del entry['student']

        potential_combinations = [(group1['group'], group2['group'], (group1['igd'] ** 2) * (group2['igd'] ** 2))
                                  for (group1, group2) in
                                  itertools.product(potential_combinations_group1, potential_combinations_group2)
                                  if (group1['igd'] ** 2) * (group2['igd'] ** 2) > initial_igd]

        valid_combinations = []
        for entry in potential_combinations:
            value = True
            for member1 in entry[0]:
                for member2 in entry[1]:
                    if member1 == member2:
                        value = False
                        break
                if not value:
                    break
            if value:
                valid_combinations.append(value)

        if valid_combinations:
            return max(valid_combinations, key=itemgetter(1))
    return -1
