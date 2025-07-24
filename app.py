from core.chromosome import generate_chromosome
from utils.fitness import (
    calculate_fitness,
    calculate_popularity,
    chromosome_to_schedule,
    binary_to_decimal,
)
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
        chromosome = generate_chromosome(len(self.courses), 3)
        schedule = chromosome_to_schedule(chromosome, self.courses)
        total_score = calculate_fitness(schedule, self.popularity)

        return (chromosome, total_score)

    def process(self):
        population = []
        for student in self.students:
            item = self.evaluate_student(student)
            population.append(item)

        selected1_population = selection(population)

        print("-----selection", len(selected1_population))
        for item in selected1_population:
            print(item)

        children = []
        for _ in range(len(selected1_population) // 2):
            parent_items = random.sample(selected1_population, 2)
            gene, fit = parent_items[0]
            gene2, fit2 = parent_items[1]

            child1, child2 = crossover(gene, gene2)

            schedule1 = chromosome_to_schedule(child1, self.courses)
            fit_child1 = calculate_fitness(schedule1, self.popularity)

            schedule2 = chromosome_to_schedule(child2, self.courses)
            fit_child2 = calculate_fitness(schedule2, self.popularity)

            children.append((child1, fit_child1))
            children.append((child2, fit_child2))

            print("Parent1: ", gene, fit)
            print("Parent2: ", gene2, fit2)
            print("Child1: ", child1, fit_child1)
            print("Child2: ", child2, fit_child2)

        print("-----crossover", len(children))

        selected2_population = selection(children)

        print("-----selection2", len(selected2_population))
        for item2 in selected2_population:
            print(item2)
        print("mutation")
        population3 = []
        for gene3, fit3 in selected2_population:
            gene4 = mutation(gene3)
            schedule3 = chromosome_to_schedule(gene4, self.courses)
            fit4 = calculate_fitness(schedule3, self.popularity)
            population3.append((gene4, fit4))
            print(gene4, fit4)
        print("-----mutation", len(population3))

        win = max(population3, key=lambda x: x[1])
        print("win: ", win)
        return win

    def output(self, chromosome):
        result = [["" for _ in range(7)] for _ in range(5)]

        for i in range(0, len(chromosome[0]) - 3 + 1, 3):
            string = (
                str(chromosome[0][i])
                + str(chromosome[0][i + 1])
                + str(chromosome[0][i + 2])
            )
            dec = binary_to_decimal(string)
            course_index = i // 3
            course_name = self.courses[course_index].get("Course")
            tup = self.courses[course_index].get("Slots")[dec]
            result[tup[1] - 1][tup[0]] = course_name
        print(result)
        return result


if __name__ == "__main__":
    solution = Solution()
    winner = solution.process()
    res = solution.output(winner)
