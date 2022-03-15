from statistics import mean

from AlgorithmTeamFormation.helping_functions.calculate_euclidean_distance import calculate_euclidean_distance


def criterion_calculation_case_2(group, student, weights):
    # Works the same as the criterion_calculation algorithm except that it doesn't consider whether igd meets the
    # threshold pt
    igd = 0
    gad = []
    for member in group:
        ed = calculate_euclidean_distance(student[1], member[1], weights)
        igd += ed
        gad.append(ed)

    gad = mean(gad)
    return igd, gad
