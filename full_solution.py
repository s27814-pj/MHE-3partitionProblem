import copy
import itertools

from goal import goal


def generate_permutations(data):
    for perm in itertools.permutations(data):
        yield perm

def full_solution(list_of_units):
    list_of_indexes_available =[]
    current_list=copy.deepcopy(list_of_units)
    best_list=copy.deepcopy(list_of_units)
    for i in range(len(list_of_units)):
        list_of_indexes_available.append(int(i%(len(list_of_units)/3)))
    count=0
    for count, perm in enumerate(generate_permutations(list_of_indexes_available)):
        for j in range(len(list_of_indexes_available)):
            current_list[j].set_index(perm[j])
        if goal(current_list) > goal(best_list):
            best_list=copy.deepcopy(current_list)
        if goal(best_list) == len(list_of_units)/3:
            break
    return best_list, count