from database_classes import Weights
import re


def none_all_or_weekdays(schedule):
    # Check to make sure the user chooses one of the three options:
    # 1. None
    # 2. All
    # 3. A combination of weekdays
    if schedule:
        for element in schedule:
            if element == 'None' and len(schedule) > 1:
                return False
            elif element == 'All' and len(schedule) > 1:
                return False
        return True
    else:
        return False


def transform_ranking_to_weights(rank_gender, rank_age, rank_experience, rank_edu_level, rank_major, rank_attempt,
                                 rank_teammate, rank_schedule, matriculation_number):
    sum_of_ranks = rank_gender + rank_age + rank_experience + rank_edu_level + rank_major + rank_attempt + \
                   rank_teammate + rank_schedule
    return Weights(rank_age / sum_of_ranks, rank_gender / sum_of_ranks, rank_attempt / sum_of_ranks, rank_edu_level /
                   sum_of_ranks, rank_major / sum_of_ranks, rank_teammate / sum_of_ranks, rank_schedule / sum_of_ranks,
                   rank_experience / sum_of_ranks, matriculation_number), Weights(rank_gender, rank_age,
                                                                                  rank_experience, rank_edu_level,
                                                                                  rank_major, rank_attempt,
                                                                                  rank_teammate, rank_schedule,
                                                                                  matriculation_number)


def has_correct_form(teammate):
    return re.match('^[0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]$', teammate)


def locate_group(group_configuration, matriculation_number):
    for group_tuple in group_configuration.items():
        for index, team_member_dict in enumerate(group_tuple[1][:-1]):
            converted_num = "{}".format(index + 1)
            key = str('Team member ' + converted_num)
            if team_member_dict[key] == matriculation_number:
                return group_tuple
    return None


def condense_group(group):
    dictionary = {}
    for element in group:
        key = list(element.keys())[0]
        value = list(element.values())[0]
        dictionary[key] = value
    return dictionary


def analyze_gad_igd(group_configuration):
    igd_values = []
    gad_values = []

    for index, group_tuple in enumerate(group_configuration.items()):
        data = group_tuple[1][-1]
        igd_values.append(data['Data']['igd'])
        gad_values.append(data['Data']['gad'])
    return igd_values, gad_values
