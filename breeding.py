import random


def breed_by_prob(p1, p2):
    child = []
    for gene1, gene2 in zip(p1, p2):
        prob_of_parent = random.random()
        if prob_of_parent <= 0.5:
            child.append(gene1)
        else:
            child.append(gene2)
    return child


def breed_by_splice(p1, p2):
    half_of_genes = len(p1)//2
    p1_splice = p1[:half_of_genes]
    p2_splice = p2[half_of_genes:]
    child = p1_splice
    child.extend(p2_splice)
    return child


def breed_by_random(p1, p2):
    rand_splice_min = random.randint(0, len(p1))
    rand_splice_max = random.randint(rand_splice_min, len(p1))
    child = p1
    p2_splice = p2[rand_splice_min:rand_splice_max]
    child[rand_splice_min:rand_splice_max] = p2_splice
    return child


if __name__ == "__main__":
    parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parent2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(parent1)
    print(parent2)
    print("\nTesting breeding by probability")
    c = breed_by_prob(parent1, parent2)
    print(c)

    print("\nTesting breeding by splicing")
    c = breed_by_splice(parent1, parent2)
    print(c)

    print("\nTesting breeding by random splicing")
    c = breed_by_random(parent1, parent2)
    print(c)
