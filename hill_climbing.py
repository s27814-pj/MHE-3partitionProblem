import copy
import random

from generate_neighbours import generate_neighbours
from goal import goal


def hill_climbing(list_of_units, random_start=False):

    current_list=copy.deepcopy(list_of_units)

    if random_start:
        list_of_indexes_available = []
        for i in range(len(list_of_units)):
            list_of_indexes_available.append(int(i % (len(list_of_units) / 3)))
        random.shuffle(list_of_indexes_available)
        for j in range(len(list_of_indexes_available)):
            current_list[j].set_index(list_of_indexes_available[j])

    counter=0
    best_neighbour=copy.deepcopy(current_list)
    better_neighbour = True
    while better_neighbour:
        list_of_neighbours=generate_neighbours(current_list)
        for neighbour in list_of_neighbours:
            counter+=1
            if goal(neighbour) > goal(best_neighbour):
                best_neighbour=copy.deepcopy(neighbour)
        if goal(best_neighbour) > goal(current_list):
            current_list=copy.deepcopy(best_neighbour)
        else:
            better_neighbour = False
    return current_list, counter



def hill_climbing_random_neighbour(list_of_units, random_start=False, max_iterations=10000):

    current_list=copy.deepcopy(list_of_units)

    if random_start:
        list_of_indexes_available = []
        for i in range(len(list_of_units)):
            list_of_indexes_available.append(int(i % (len(list_of_units) / 3)))
        random.shuffle(list_of_indexes_available)
        for j in range(len(list_of_indexes_available)):
            current_list[j].set_index(list_of_indexes_available[j])

    counter=0
    best_neighbour=copy.deepcopy(current_list)
    better_neighbour = True
    while better_neighbour:
        list_of_neighbours=generate_neighbours(current_list)
        for neighbour in list_of_neighbours:
            counter+=1
            if goal(neighbour) > goal(best_neighbour):
                best_neighbour=copy.deepcopy(neighbour)
            elif (goal(neighbour) == goal(best_neighbour) and
                  random.randint(0, len(list_of_units)) >=counter%len(list_of_units)):
                best_neighbour = copy.deepcopy(neighbour)
        if goal(best_neighbour) > goal(current_list):
            current_list=copy.deepcopy(best_neighbour)
        elif (goal(current_list) == goal(best_neighbour)
              # and random.randint(0, 100) < 50
              and counter < max_iterations):
            current_list=copy.deepcopy(best_neighbour)
        else:
            better_neighbour = False
        if goal(current_list) == len(list_of_units)/3: better_neighbour=False
    return current_list, counter
