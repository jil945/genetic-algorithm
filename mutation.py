import random


def random_mutation(fitness, population, begin, step):
    for i in range(len(population)):
        temp = ""
        for j in range(len(population[i])):
            temp = temp + chr(random.randint(begin, begin + step - 1))
        population[i] = temp[:]
    return population


def mutate_one(fitness, population, begin, step):
    for j in range(len(population)):
        i = int(random.randint(0, len(population[j])))
        temp = population[j][:i] + chr(random.randint(begin, begin + step - 1)) + population[j][(i + 1):]
        # above is faster than turning strings into lists of chars and back to strings
        population[j] = temp[:]
    return population


def flip_bit_all(fitness, population):  # like random_mutation except with bits
    for bits in population:
        for i in range(len(bits)):
            bits[i] = (bits[i] + 1) % 2
    return population


def flip_bit_one(fitness, population):  # like mutate_one except with bits
    for bits in population:
        select_number = random.randint(0, len(bits) - 1)
        bits[select_number] = (bits[select_number] + 1) % 2
    return population


def flip_bit_k_random_each(fitness, population):
    """
    Flips K random bits in rounds
    Ex. [1, 0, 1] flips K random bits in 30 or less rounds
    [1, 0] flips K random bits in 20 or less rounds
    etc.
    """
    for bits in population:
        rounds = random.randint(0, len(bits)*10)
        count = 0
        while count < rounds:
            select_number = random.randint(0, len(bits) - 1)
            bits[select_number] = (bits[select_number] + 1) % 2
            count += 1
    return population


if __name__ == '__main__':
    import copy


    def _generateWord(length, begin, step):
        return "".join([chr(random.randint(begin, begin + step - 1)) for _ in range(length)])


    def initialPop(sizePop, lengthOfChild, begin, step):
        return [_generateWord(lengthOfChild, begin, step) for _ in range(sizePop)]


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


    pop = [[1, 0, 0], [1, 0, 1], [0, 1, 1]]
    pop2 = copy.deepcopy(pop)
    pop3 = copy.deepcopy(pop)
    print(random_mutation(f, initialPop(10, len(password), 97, 26), 97, 26))
    print(mutate_one(f, initialPop(10, len(password), 97, 26), 97, 26))
    print(flip_bit_all(f, pop))
    print(flip_bit_one(f, pop2))
    print(flip_bit_k_random_each(f, pop3))
    """
    child1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    genes = [i for i in range(100)]
    random_mutation(child1, genes)
    print(child1)
    """
