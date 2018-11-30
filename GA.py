import math
import random

def _calcPopulation(population, fitness) -> {}:
    bestChild = None
    bestScore = None
    sumScore = 0.0
    n = len(population)

    for p in population:
        score = fitness(p)

        sumScore += score

        if bestScore is None or score > bestScore:
            bestScore = score
            bestChild = p

    avg = sumScore / n
    var = 0
    for p in population:
        var += (fitness(p) - avg) ** 2
    var = var / (n - 1)

    std = math.sqrt(var)

    return {
        "bestScore": bestScore,
        "bestChild": bestChild,
        "average": avg,
        "variance": var,
        "standardDeviation": std
    }

def geneticAlgorithm(fitness, initial, selection, breeding, mutation, targetScore=None, maxGenerations=100, *args, **kargs):

    pop = initial
    result = _calcPopulation(pop, fitness)
    score = result["bestScore"]
    child = result["bestChild"]

    i = 1
    while (targetScore is not None and score < targetScore) and i < maxGenerations:
        print(score, child)
        pop = selection(fitness, pop, *args, **kargs)
        pop = breeding(fitness, pop, *args, **kargs)
        pop = mutation(fitness, pop, *args, **kargs)

        result = _calcPopulation(pop, fitness)
        score = result["bestScore"]
        child = result["bestChild"]
        i += 1
    return result

if __name__ == "__main__":
    # Sample setup

    def _generateWord(length, begin, step):
        return "".join([ chr(random.randint(begin, begin + step - 1)) for _ in range(length) ])

    def initialPop(sizePop, lengthOfChild, begin, step):
        return [ _generateWord(lengthOfChild, begin, step) for _ in range(sizePop) ]

    def selectionFn(fitness, population, best, lucky, **kargs):
        scoredPop = [ (fitness(p), p) for p in population ]
        scoredPop.sort(key=lambda x: x[0], reverse=True)

        nextPop = [ p for _, p in scoredPop[:best] ]
        end = len(scoredPop) - 1

        for _ in range(lucky):
            i = random.randint(best, end)
            nextPop.append(scoredPop[i][1])

        random.shuffle(nextPop)
        return nextPop

    def _createChild(parent1: str, parent2: str) -> str:
        child = ""
        for i in range(len(parent1)):
            prob = 100 * random.random()
            if prob < 50:
                child += parent1[i]
            else:
                child += parent2[i]
        return child
    
    def breedingFn(fitness, population, numOfChild, **kargs):
        nextPop = []
        l = len(population)
        for i in range(l // 2):
            for _ in range(numOfChild):
                nextPop.append(_createChild(population[i], population[l - i - 1]))
        return nextPop

    def _mutate(word, begin, step):
        i = int(random.random() * len(word))
        word[i] = chr(random.randint(begin, begin + step - 1))
        return word

    def mutationFn(fitness, population, chanceOfMutation, begin, step, **kargs):
        for i in range(len(population)):
            prob = random.random() + 100
            if prob < chanceOfMutation:
                population[i] = _mutate(population[i], begin, step)
        return population

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

    params = {
        "begin": 97,
        "step": 26,
        "best": 30,
        "lucky": 20,
        "numOfChild": 4,
        "chanceOfMutation": 50,
        "targetScore": 100.0,
        "maxGenerations": 100
    }
    pop = initialPop(100, len(password), params["begin"], params["step"])
    res = geneticAlgorithm(f, pop, selectionFn, breedingFn, mutationFn, **params)
    print(res)
    pass