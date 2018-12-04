import random

"""
def breed_by_prob(parent1, parent2):
    child = []
    for p1, p2 in zip(parent1, parent2):
        prob_of_parent = random.random()
        if prob_of_parent <= 0.45:
            child.append(p1)
        elif prob_of_parent <= 0.90:
            child.append(p2)
        else:
            child.append(mutate_children())
    return child
"""


def breed_by_splice(p1, p2):
    half_of_genes = len(p1)//2
    p1_splice = p1[:half_of_genes]
    p2_splice = p2[:half_of_genes]
    p1[:half_of_genes] = p2_splice
    p2[:half_of_genes] = p1_splice


def breed_by_random(p1, p2):
    rand_splice_min = random.randint(0, len(p1))
    rand_splice_max = random.randint(rand_splice_min, len(p1))
    p1_splice = p1[rand_splice_min:rand_splice_max]
    p2_splice = p2[rand_splice_min:rand_splice_max]
    p1[rand_splice_min:rand_splice_max] = p2_splice
    p2[rand_splice_min:rand_splice_max] = p1_splice


if __name__ == "__main__":
    parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parent2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    alt_parent1 = parent1[:]
    alt_parent2 = parent2[:]
    breed_by_splice(parent1, parent2)
    print("Parent 1: {}\nParent 2: {}\n".format(parent1, parent2))
    breed_by_random(alt_parent1, alt_parent2)
    print("Alternate Parent 1: {}\nAlternate Parent 2: {}\n".format(alt_parent1, alt_parent2))
    parent1[10:10] = []
    print(parent1)
