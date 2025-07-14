import random
def crossover(parent1, parent2, crossover_rate = 0.9):
    length = len(parent1)
    child1 = parent1.copy()
    child2 = parent2.copy()

    for i in range(length):
        if random.random() < crossover_rate:
            child1[i], child2[i] = child2[i], child1[i]
    return child1, child2