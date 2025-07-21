import random

def generate_chromosome(course_num, bit_num):
    genes = []
    for _ in range(course_num*bit_num):
        random_index = random.randint(0,1)
        genes.append(random_index)
    return genes