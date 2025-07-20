from core.chromosome import Chromosome
from utils.fitness import calculate_fitness, calculate_popularity, build_schedule
from utils.loader import load_courses, load_students, DAY_NAMES
from core.selection import selection
from core.crossover import crossover
from core.mutation import mutation
import random


class Solution:
    def __init__(
        self, courses_file="./data/courses.csv", students_file="./data/students.csv"
    ):
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
            # random
            # calc fitness
            population.append(item)

        selected1_population = selection(population) # (gen, fit)[]

        print("-----selection", len(selected1_population))
        for item in selected1_population:
            print(item)

        children = []
        for _ in range(len(selected1_population) // 2):
            parent_items = random.sample(selected1_population, 2)
            gene, fit = parent_items[0]
            gene2, fit2 = parent_items[1]

            child1, child2 = crossover(gene, gene2)
            # calc fit
            fit_child1 = self.evaluate_student(child1)
            fit_child2 = self.evaluate_student(child2)

            children.append((child1, fit_child1))
            children.append((child2, fit_child2))

            print("Parent1: ", gene, fit)
            print("Parent2: ", gene2, fit2)
            print("Child1: ", fit_child1)
            print("Child2: ", fit_child2)

        print("-----crossover", len(children))
        
        # ???
        population2 = []
        for student2 in children:
            item2 = self.evaluate_student(student2)
            population2.append(item2)

        selected2_population = selection(population2)

        print("-----selection2", len(selected2_population))
        for item2 in selected2_population:
            print(item2)
        print("mutation")
        population3 = []
        for gene3, fit3 in selected2_population:
            gene4 = mutation(gene3)
            fit4 = self.evaluate_student(gene4)
            population3.append((fit4))
            print('test', gene3, gene4, fit4)
        print("-----mutation", len(population3)) # (gene, fit)[]
        # mutated1 = mutation(child1)
        # mutated2 = mutation(child2)
        # print(mutated1, mutated2)
        win = max(population3, key=lambda x: x[1])
        print("win: ", win)
        # post-processing gene ==> timetable data
        # [
        #     ["Math", "Physics", "Chemistry", "Biology", "English", "", ""],
        #     ["", "PE", "Math", "Physics", "", "", ""],
        #     ["Literature", "", "Music", "", "History", "", ""],
        #     ["", "", "", "", "", "", ""],
        #     ["Art", "", "", "", "Math", "", ""],
        # ]

if __name__ == "__main__":
    solution = Solution()
    solution.process()
