from core.chromosome import Chromosome
from utils.fitness import (
    calculate_fitness,
    calculate_popularity,
    build_schedule
)
from utils.loader import load_courses, load_students, DAY_NAMES
from core.selection import selection
from core.crossover import crossover
from core.mutation import mutation
import random

class Solution:
    def __init__(self, courses_file="./data/courses.csv", students_file="./data/students.csv"):
        self.courses = load_courses(courses_file)
        self.students = load_students(students_file)
        self.popularity = calculate_popularity(self.students)

    def evaluate_student(self, student):
        chromosome = Chromosome(self.courses)
        schedule = build_schedule(chromosome, self.courses)
        reward, penalty = calculate_fitness(schedule, self.popularity)
        total_score = reward + penalty

        genes_binary = chromosome.binary_array(self.courses)
        return (genes_binary, total_score)

    def process(self):
        population = []
        for student in self.students:
            item = self.evaluate_student(student)
            population.append(item) 
        
        selected1_population = selection(population)

        for _ in range(len(selected1_population)):
            # pick random 2
            # chay crossover
            # test
            parent_items = random.sample(selected1_population, 2)
            # parent_items = [(gene[], fit), (gene2[], fit2)]
            gene, fit = parent_items[0]
            gene2, fit2 = parent_items[1]
            child1, child2 = crossover(gene, gene2)
            mutated1 = mutation(child1)
            mutated2 = mutation(child2)
        print(gene, fit)
        print(gene2, fit2)
        print(child1, child2)
        print(mutated1, mutated2)
        


        # print('-----', len(test))
        # for item in test:
        #     print(item)

if __name__ == "__main__":
    solution = Solution()
    solution.process()