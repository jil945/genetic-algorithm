import random


def elite_selection(fitness, population):
    scoredPop = sorted(population, key=fitness, reverse=True)

    selection = int((.1 * len(population)))
    return scoredPop[:selection]

def best_half_selection(fitness, population):
    scoredPop = sorted(population, key=fitness, reverse=True)

    selection = int((.5 * len(population)))
    return scoredPop[:selection]


def random_kth_selection(fitness, population):
    scoredPop = sorted(population, key=fitness, reverse=True)
    selection = int((random.random() * len(population))) + 2

    return scoredPop[:selection]


def random_choice_selection(fitness, population):
    random_candidates = []
    select_number = int((random.random() * len(population))) + 2
    for _ in range(select_number):
        random_candidates.append(random.choice(population))
    return random_candidates


if __name__ == "__main__":
    def _generateWord(length, begin, step):
        return "".join([ chr(random.randint(begin, begin + step - 1)) for _ in range(length) ])

    def initialPop(sizePop, lengthOfChild, begin, step):
        return [ _generateWord(lengthOfChild, begin, step) for _ in range(sizePop) ]


    password = "helloworld"
    def f(word):
        if len(word) != len(password):
            return 0.0
        else:
            score = 0
            for i, p in enumerate(password):
                if p == word[i]:
                    score += 1
            return score * 100 / len(password)

    print(elite_selection(f, initialPop(10, len(password), 97, 26)))
    print(best_half_selection(f, initialPop(10, len(password), 97, 26)))
    print(random_kth_selection(f, initialPop(10, len(password), 97, 26)))
    print(random_choice_selection(f, initialPop(10, len(password), 97, 26)))

    """ pop = []
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
        print(i + 1, new_pop[i]) """
