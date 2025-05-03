import copy
import random

from generate_neighbours import generate_neighbours, generate_neighbours2
from goal import goal, goal2
# from goal import goal3 as goal2


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
        list_of_neighbours = [n for n in generate_neighbours2(current_index) if n not in tabu_list]
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
    return best_index, counter