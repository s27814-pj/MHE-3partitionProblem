import sys
import copy
import random
from collections import Counter

from full_solution import full_solution
from hill_climbing import hill_climbing, hill_climbing_random_neighbour
from random_solution import random_solution
from tabu_search import tabu_search
from unit import Unit
from goal import goal
from generate_neighbours import generate_neighbours

def read_from_file():
    with open('inputData.txt', 'r') as file:
        line = file.readline().strip()
    return line.split(',')

def fix_values_to_triplets(values):
    if (len(values) % 3)==2 :
        values.append(values[0])
    if (len(values) % 3)==1:
        values.append(values[0])
        values.append(values[0])
    return values

def assign_index_to_values(values):
    list_of_units=[]
    for i in range(len(values)):
        list_of_units.append(Unit(values[i], int(i%(len(values)/3))))
    return list_of_units



def main():
    if len(sys.argv) < 2:
        print("No arguments given, will use inputData.txt")
        values = read_from_file()
    elif sys.argv[1] == '--random':
        print("Will use 12 random values as input [20..45]")
        values = [random.randint(20, 45) for _ in range(12)]
    elif (len(sys.argv)-1)%3 !=0:
        print("Invalid number of arguments, needs 3kN, will append first value to make 3kN")
        values = [int(arg) for arg in sys.argv[1:]]
    elif (len(sys.argv)-1)%3 ==0:
        values = [int(arg) for arg in sys.argv[1:]]
    values=fix_values_to_triplets(values)
    list_of_units = assign_index_to_values(values)
    print('Values with index of their triplet\n',list_of_units)
    print('Value of goal() for given input:', goal(list_of_units))
    print('press 1 to generate neighbours for input')
    print('press 2 for random solution')
    print('press 3 for full solution')
    print('press 4 for hill_climbing solution')
    print('press 5 for hill_climbing solution with random starting point')
    print('press 6 for hill_climbing solution with random chosen neighbours')
    print('7 for tabu search')
    user_input = input()
    match user_input:
        case '1':
            for n in generate_neighbours(list_of_units):
                print(n)
        case '2':
            list_from_random_solution, counter_from_random_solution = random_solution(list_of_units, 10000)
            print('goal of random solution:', goal(list_from_random_solution),
                  ' counter:', counter_from_random_solution,
                  '\nRandom Solution\n', list_from_random_solution)
        case '3':
            if (len(list_of_units)) >12:
                print('skipping full solution, too big input')
            else:
                list_from_full_solution, counter_from_full_solution=full_solution(list_of_units)
                print('goal of full solution:', goal(list_from_full_solution),
                  ' counter:', counter_from_full_solution,
                  '\nFull Solution\n', list_from_full_solution)
        case '4':
            list_from_hill_climbing, counter_from_hill_climbing = hill_climbing(list_of_units)
            print('goal of hill climbing:', goal(list_from_hill_climbing),
                  ' counter:', counter_from_hill_climbing,
                  '\nHill Climbing Solution\n', list_from_hill_climbing)
        case '5':
            list_from_hill_climbing, counter_from_hill_climbing = hill_climbing(list_of_units, True)
            print('goal of hill climbing:', goal(list_from_hill_climbing),
                  ' counter:', counter_from_hill_climbing,
                  '\nHill Climbing Solution\n', list_from_hill_climbing)
        case '6':
            list_from_hill_climbing, counter_from_hill_climbing = hill_climbing_random_neighbour(list_of_units)
            print('goal of hill climbing rand neighbour:', goal(list_from_hill_climbing),
              ' counter:', counter_from_hill_climbing,
              '\nHill Climbing Solution with rand neighbour\n', list_from_hill_climbing)
        case '7':
            list_from_tabu_search, counter_from_tabu_search = tabu_search(list_of_units)
            print('goal of tabu search:', goal(list_from_tabu_search),
                  ' counter:', counter_from_tabu_search,
                  '\nTabu Search\n', list_from_tabu_search)


if __name__ == '__main__':
    main()