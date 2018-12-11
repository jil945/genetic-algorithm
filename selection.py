import random


def elite_selection(fitness, population, **kargs):
    scored_pop = sorted(population, key=fitness, reverse=True)

    selection = int((.1 * len(population)))
    return scored_pop[:selection]

def best_half_selection(fitness, population, **kargs):
    scored_pop = sorted(population, key=fitness, reverse=True)

    selection = int((.5 * len(population)))
    return scored_pop[:selection]


def random_kth_selection(fitness, population, **kargs):
    scored_pop = sorted(population, key=fitness, reverse=True)
    selection = int((random.random() * len(population))) + 2

    return scored_pop[:selection]


def random_choice_selection(fitness, population, **kargs):
    random_candidates = []
    select_number = int((random.random() * len(population))) + 2
    for _ in range(select_number):
        random_candidates.append(random.choice(population))
    return random_candidates


if __name__ == "__main__":
    fitness = lambda x : random.randint(0, 50)
    pop = []
    new_pop = []
    for _ in range(100):
        child = [random.randint(0, 50) for _ in range(10)]
        pop.append(child)
    print("Testing pop")
    for i in range(10):
        print(i + 1, pop[i])

    print("\nTesting elite selection")
    new_pop = elite_selection(fitness, pop)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting half selection")
    new_pop = best_half_selection(fitness, pop)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting random kth selection")
    new_pop = random_kth_selection(fitness, pop)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting random choice selection")
    new_pop = random_choice_selection(fitness, pop)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])
