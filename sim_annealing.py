import math
import random

from generate_neighbours import generate_neighbours2
from goal import goal2
# from goal import goal3 as goal2

def temperature(i):
    return 1000.0/i

def annealing(values,index, steps=1000):
    current_index = index.copy()
    solutions= [current_index]
    for i in range(1,steps):
        list_of_neighbours=generate_neighbours2(current_index)
        rand = random.randint(0, len(list_of_neighbours) - 1)
        if goal2(values, list_of_neighbours[rand]) >= goal2(values, current_index):
            current_index=list_of_neighbours[rand].copy()
        solutions.append(current_index)

    best_solution=solutions[0]
    for s in solutions:
        if goal2(values,s) > goal2(values,best_solution):
            best_solution = s.copy()

    return best_solution, steps