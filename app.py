from core.chromosome import Chromosome
from utils.fitness import (
    calculate_fitness,
    calculate_popularity,
    build_schedule
)
from utils.loader import load_courses, load_students, DAY_NAMES

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
        results = []
        for student in self.students:
            result = self.evaluate_student(student)
            results.append(result)
        for item in results:
            print(item)

if __name__ == "__main__":
    solution = Solution()
    solution.process()