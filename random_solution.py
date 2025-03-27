import copy
import random

from goal import goal


def random_solution(list_of_units, max_iterations):
    list_of_indexes_available =[]
    current_list=copy.deepcopy(list_of_units)
    best_list=copy.deepcopy(list_of_units)

    for i in range(len(list_of_units)):
        list_of_indexes_available.append(int(i%(len(list_of_units)/3)))
    random.shuffle(list_of_indexes_available)

    i=0
    for i in range(max_iterations):
        for j in range(len(list_of_indexes_available)):
            current_list[j].set_index(list_of_indexes_available[j])
        if goal(current_list) > goal(best_list):
            best_list=copy.deepcopy(current_list)
        if goal(best_list) == len(list_of_units)/3:
            break
        random.shuffle(list_of_indexes_available)
    return best_list, i