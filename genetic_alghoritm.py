import random
import heapq
import statistics

from goal import goal2, goal3


def init_pop(index,n):
    pop=index.copy()
    population = []
    for i in range(n):
        random.shuffle(pop)
        population.append(pop.copy())
    return population

def tournament_selection(population,population_fitness, tournament_size=4):
    individual=max(random.sample(list(zip(population, population_fitness)), tournament_size), key=lambda x: x[1])[0]
    return individual

def crossover(parent1,parent2):
    #na parenta 1 nałóź wybrane zbiory parenta2, zapisz pozycje gdzie wkładasz, na stos wrzuc zamieniona wartosc,
    # na koniec przejrzyj childa z pominieciem pozycji zamian, jezeli index z tej grupy co przejal to ze
    # zastap wartoscia ze stosu - chyba ze ta sama wartosc pomin
    random_parts = random.randint(0, int((len(parent1) / 3) * 0.7))
    stack=[]
    child=parent1.copy()
    for i in range(random_parts):
        inherited_index=random.randint(0, int(len(parent1)/3)-1)
        positions_in_parent=[]
        for ii in range(len(parent2)):
            if parent2[ii] == inherited_index: positions_in_parent.append(ii)
        for p in positions_in_parent:
            if child[p]==inherited_index :continue
            stack.append(child[p])
            child[p]=inherited_index
        for j in range(len(child)):
            if j in positions_in_parent: continue
            if child[j]==inherited_index: child[j]=int(stack.pop())
            # print(sum(child))
    return child

def crossover2(parent1, parent2, n=4):
#     na parenta1 nalozyc pierwszy element parenta2, przeszykac dalej i zmienc wartosc pierwszo wystapeinia ++dalej

    child=parent1.copy()
    for i in range(n):
        tmp=child[i]
        child[i]=parent2[i]
        for j in range(i+1, len(child)):
            if child[j]==parent2[i]:
                child[j]=tmp
                break
    # print(sum(child))
    return child

def crossover3(parent1, parent2, n=4):
#     na parenta1 nalozyc pierwszy element parenta2, przeszykac dalej i zmienc wartosc pierwszo wystapeinia ++dalej
    rand_start=random.randint(0,len(parent1)-1)
    rand_end=random.randint(0,len(parent1)-1)
    if rand_start > rand_end:
        rand_start, rand_end = rand_end, rand_start
    child=parent1.copy()
    for i in range(rand_start, rand_end):
        tmp=child[i]
        child[i]=parent2[i]
        found= False
        for j in range(0, i):
            if child[j]==parent2[i]:
                child[j]=tmp
                found=True
                break
        if not found:
            for j in range(i+1, len(child)):
                if child[j] == parent2[i]:
                    child[j] = tmp
                    found = True
                    break

    # print(sum(child))
    return child



def mutate(individual, mutation_rate=0.1):
    if random.random() > mutation_rate: return individual
    stack = []
    child=individual.copy()
    mutated_index = random.randint(0, int(len(child) / 3) - 1)
    mutated_index_new=random.randint(0, int(len(child) / 3) - 1)
    mutated_positions = []
    for i in range(len(child)):
        if child[i]==mutated_index : mutated_positions.append(i)
    for p in mutated_positions:
        if child[p] == mutated_index_new: continue
        stack.append(child[p])
        child[p]=mutated_index_new
    for i in range(len(child)):
        if i in mutated_positions: continue
        if child[i]==mutated_index_new: child[i]=int(stack.pop())
    return child

def mutate2(individual, mutation_rate=0.01):
    child = individual.copy()
    for i in range(len(child)):
        if random.random() > mutation_rate: continue
        random_index=random.randint(0, int(len(child) / 3) - 1)
        tmp=child[i]
        child[i]=random_index
        for j in range(len(child)):
            if j==i:continue
            if child[j]==random_index:
                child[j]=tmp
                break
    # print(sum(child))
    return child


def genetic_algorithm(values, index, population_size=700, generations=40):
    population = init_pop(index,population_size)
    population_fitness = []
    for p in population:
        population_fitness.append(goal3(values,p))

    best_individual = max(list(zip(population, population_fitness)), key=lambda x: x[1])[0]

    for gen in range(generations):
        new_population = []
        new_population_fitness=[]
        for _ in range(population_size):
            parent1 = tournament_selection(population, population_fitness)
            parent2 = tournament_selection(population, population_fitness)

            child = crossover3(parent1, parent2)
            child = mutate2(child)

            new_population.append(child)

        for p in new_population:
            new_population_fitness.append(goal3(values, p))

        best_individual_new_population = max(list(zip(new_population, new_population_fitness)), key=lambda x: x[1])[0]
        if goal3(values,best_individual_new_population)>goal3(values,best_individual):best_individual=best_individual_new_population
        # print('best score', goal3(values,best_individual_new_population),'in generation ', gen, best_individual_new_population, 'variance(*-1) among generation', statistics.variance(new_population_fitness)*(-1))
        if goal3(values,best_individual)>=0: return best_individual, gen
        population = new_population

    return best_individual, generations
