import copy
import random

from generate_neighbours import generate_neighbours, generate_neighbours2
from goal import goal, goal2


def exists_in_tabu(tabu_list, unit_list):
    unit_tuple = tuple((unit.get_value(), unit.get_index()) for unit in unit_list)
    for tabu in tabu_list:
        tabu_tuple = tuple((unit.get_value(), unit.get_index()) for unit in tabu)
        if unit_tuple == tabu_tuple:
            return True
    return False

def tabu_search_old(list_of_units, max_iterations=1000, tabu_size=1000, random_start=False, go_backwards=True):
    best_list = copy.deepcopy(list_of_units)

    if random_start:
        list_of_indexes_available = []
        for i in range(len(list_of_units)):
            list_of_indexes_available.append(int(i%(len(list_of_units)/3)))
        random.shuffle(list_of_indexes_available)
        for j in range(len(list_of_indexes_available)):
            best_list[j].set_index(list_of_indexes_available[j])

    tabu_list=[]
    counter=0
    current_list=copy.deepcopy(best_list)
    tabu_list.append(current_list)
    i=0
    while i< max_iterations and goal(best_list) < len(list_of_units)/3:
        list_of_neighbours=[ n for n in generate_neighbours(current_list) if not exists_in_tabu(tabu_list, n) ]
        # print(len(list_of_neighbours), i)
        if len(list_of_neighbours) == 0 and go_backwards:
            for ii in range(len(tabu_list) -1, -1, -1):
                list_of_neighbours = [n for n in generate_neighbours(tabu_list[ii]) if not exists_in_tabu(tabu_list, n)]
                i+=1
                if len(list_of_neighbours)>0: break
        elif len(list_of_neighbours) == 0: break
        best_neighbour = list_of_neighbours[0]
        for neighbour in list_of_neighbours:
            counter+=1
            if goal(best_neighbour) < goal(neighbour):
                best_neighbour = neighbour.copy()
        if goal(best_neighbour) >= goal(best_list):
            best_list=best_neighbour.copy()
        current_list = copy.deepcopy(best_neighbour)
        tabu_list.append(best_neighbour)
        i=i+1
        if len(tabu_list) > tabu_size:tabu_list.pop(0)
        # print(i ,best_list, "goal=", goal(best_list))
    return best_list, counter

def tabu_search(values, index, max_iterations=1000, tabu_size=100, random_start=False, go_backwards=True):
    best_index = index.copy()

    if random_start:
        list_of_indexes_available = []
        for i in range(len(values)):
            list_of_indexes_available.append(int(i % (len(values) / 3)))
        random.shuffle(list_of_indexes_available)
        for j in range(len(list_of_indexes_available)):
            best_index=list_of_indexes_available.copy()


    tabu_list=[]
    counter=0
    current_index=best_index.copy()
    tabu_list.append(current_index)
    i=0
    while i< max_iterations and goal2(values, best_index) < len(best_index)/3:
        # list_of_neighbours=[ n for n in generate_neighbours(current_index) if not in tabu_list]
        list_of_neighbours = [n for n in generate_neighbours2(current_index) if n not in tabu_list]
        # print(len(list_of_neighbours), i)
        if len(list_of_neighbours) == 0 and go_backwards:
            for ii in range(len(tabu_list) -1, -1, -1):
                list_of_neighbours = [n for n in generate_neighbours(tabu_list[ii])if n not in tabu_list]
                i+=1
                if len(list_of_neighbours)>0: break
        elif len(list_of_neighbours) == 0: break
        best_neighbour = list_of_neighbours[0].copy()
        for neighbour in list_of_neighbours:
            counter+=1
            if goal2(values, best_neighbour) < goal2(values, neighbour):
                best_neighbour = neighbour.copy()
        if goal2(values, best_neighbour) >= goal2(values, best_index):
            best_index=best_neighbour.copy()
        current_index = best_neighbour.copy()
        tabu_list.append(best_neighbour)
        i=i+1
        if len(tabu_list) > tabu_size:tabu_list.pop(0)
        # print(i ,best_list, "goal=", goal(best_list))
    return best_index, counter