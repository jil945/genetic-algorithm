import random


def elite_selection(children, pop_number):
    elite_candidates = []
    selection = int((.1 * pop_number))
    elite_candidates.extend(children[:selection])
    return elite_candidates


def best_half_selection(children, pop_number):
    best_half_candidates = []
    selection = int((.5 * pop_number))
    best_half_candidates.extend(children[:selection])
    return best_half_candidates


def random_kth_selection(children, pop_number):
    random_candidates = []
    selection = int((random.random() * pop_number))
    if selection == 0:
        selection += 2
    random_candidates.extend(children[:selection])
    return random_candidates


def random_choice_selection(children, pop_number):
    random_candidates = []
    select_number = int((random.random() * pop_number))
    if select_number == 0:
        select_number += 2
    for _ in range(select_number):
        random_candidates.append(random.choice(children))
    return random_candidates


if __name__ == "__main__":
    pop = []
    new_pop = []
    for _ in range(100):
        child = [random.randint(0, 50) for _ in range(10)]
        pop.append(child)
    print("Testing pop")
    for i in range(10):
        print(i + 1, pop[i])

    print("\nTesting elite selection")
    new_pop = elite_selection(pop, 50)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting half selection")
    new_pop = best_half_selection(pop, 50)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting random kth selection")
    new_pop = random_kth_selection(pop, 50)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])

    print("\nTesting random choice selection")
    new_pop = random_choice_selection(pop, 50)
    for i in range(len(new_pop)):
        print(i + 1, new_pop[i])
