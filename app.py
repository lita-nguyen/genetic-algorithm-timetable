from core.chromosome import Chromosome
from utils.fitness import (
    calculate_fitness,
    calculate_popularity,
    map_chromosome_to_schedule
)
from utils.loader import load_courses, load_students, DAY_NAMES

class Solution:
    def __init__(self, courses_file="./data/courses.csv", students_file="./data/students.csv"):
        self.courses = load_courses(courses_file)
        self.students = load_students(students_file)
        self.popularity = calculate_popularity(self.students)

    def evaluate_student(self, student):
        chromosome = Chromosome(self.courses)
        schedule = map_chromosome_to_schedule(chromosome, self.courses)
        reward, penalty = calculate_fitness(schedule, self.popularity)
        total_score = reward + penalty

        print(f"\nSinh viên: {student['name']}")
        print(f"Tổng điểm: {total_score} (Reward: {reward}, Penalty: {penalty})")
        print("Lịch học:")
        for course, (day, slot) in schedule.items():
            preference = student["schedule"].get((day, slot), 0)
            popularity_score = self.popularity.get((day, slot), 0)
            print(f"  - {course}: {DAY_NAMES[day]} {slot} (popularity: {popularity_score}, preference: {preference})")

        print("Gene nhị phân:")
        print(chromosome)
        print("-" * 40)

    def process(self):
        for student in self.students:
            self.evaluate_student(student)

if __name__ == "__main__":
    solution = Solution()
    solution.process()