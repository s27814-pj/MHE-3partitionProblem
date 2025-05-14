import copy
import random

from generate_neighbours import generate_neighbours, generate_neighbours2
from goal import goal, goal2
# from goal import goal3 as goal2


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
                #losowo pojeduynczy sasiad
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


def hill_climbing_random_neighbour2(values, index, random_start=False, max_iterations=1000):

    current_index = index.copy()
    if random_start:
        list_of_indexes_available = []
        for i in range(len(values)):
            list_of_indexes_available.append(int(i % (len(values) / 3)))
        random.shuffle(list_of_indexes_available)
        for j in range(len(list_of_indexes_available)):
            current_index=list_of_indexes_available.copy()
    counter=0
    while (counter < max_iterations):
        list_of_neighbours = generate_neighbours2(current_index)
        counter+=1
        rand=random.randint(0,len(list_of_neighbours)-1)
        if goal2(values,list_of_neighbours[rand]) >= goal2(values,current_index):
            current_index=list_of_neighbours[rand].copy()
        if goal2(values,current_index) == len(current_index) / 3: break

    return current_index, counter

def hill_climbing2(values, index, random_start=False):
    counter = 0
    current_index = index.copy()
    best_neighbour = index.copy()
    better_neighbour = True
    while better_neighbour:
        list_of_neighbours = generate_neighbours2(current_index)
        for neighbour in list_of_neighbours:
            counter += 1
            if goal2(values,neighbour) > goal2(values,best_neighbour):
                best_neighbour = neighbour.copy()
        if goal2(values,best_neighbour) > goal2(values, current_index):
            current_index = best_neighbour.copy()
        else:
            better_neighbour = False

    return current_index, counter
