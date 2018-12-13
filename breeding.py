import random

def _select_random_parents(start, end):
    p1 = random.randint(start, end - 1)
    p2 = random.randint(start, end - 1)
    while p1 == p2:
        p2 = random.randint(start, end - 1)
    return p1, p2

def _breed_prob(p1, p2, probability):
    child1 = []
    child2 = []
    for gene1, gene2 in zip(p1, p2):
        if random.random() <= probability:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)
    return child1, child2

def breeding_by_prob(fitness, population, target_pop_num, probability=0.5, **kargs):
    next_pop = []
    while len(next_pop) < target_pop_num:
        p1, p2 = _select_random_parents(0, len(population))
        # Breeding by prob
        c1, c2 = _breed_prob(population[p1], population[p2], probability)
        next_pop.append(c1)
        next_pop.append(c2)
    
    while len(next_pop) > target_pop_num:
        next_pop.pop()

    return next_pop


def _breed_splice(p1, p2):
    m = len(p1) // 2
    return p1[:m] + p2[m:], p2[:m] + p1[m:]

def breeding_by_splice(fitness, population, target_pop_num, **kargs):
    next_pop = []
    while len(next_pop) < target_pop_num:
        p1, p2 = _select_random_parents(0, len(population))
        c1, c2 = _breed_splice(population[p1], population[p2])
        next_pop.append(c1)
        next_pop.append(c2)

    while len(next_pop) > target_pop_num:
        next_pop.pop()

    return next_pop

def _breed_random_splice(p1, p2):
    start = random.randint(0, len(p1))
    end = random.randint(start, len(p1))
    child1 = p1
    child2 = p2
    child1[start:end] = p2[start:end]
    child2[start:end] = p1[start:end]
    return child1, child2

def breeding_by_random_splice(fitness, population, target_pop_num, **kargs):
    next_pop = []
    while len(next_pop) < target_pop_num:
        p1, p2 = _select_random_parents(0, len(population))
        c1, c2 = _breed_random_splice(population[p1], population[p2])
        next_pop.append(c1)
        next_pop.append(c2)

    while len(next_pop) > target_pop_num:
        next_pop.pop()

    return next_pop


if __name__ == "__main__":
    """ parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parent2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(parent1)
    print(parent2)
    print("\nTesting breeding by probability")
    c = breeding_by_prob(parent1, parent2)
    print(c)

    print("\nTesting breeding by splicing")
    c = _breed_splice(parent1, parent2)
    print(c)

    print("\nTesting breeding by random splicing")
    c = _breed_random_splice(parent1, parent2)
    print(c) """
