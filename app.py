from core.chromosome import Chromosome
from utils.fitness import (
    calculate_fitness,
    calculate_popularity,
    build_schedule
)
from utils.loader import load_courses, load_students
from core.selection import selection
from core.crossover import crossover
from core.mutation import mutation
import random

class Solution:
    def __init__(self, courses_file="./data/courses.csv", students_file="./data/students.csv"):
        self.courses = load_courses(courses_file)
        self.students = load_students(students_file)
        self.popularity = calculate_popularity(self.students)
        self.threshold = 400

    def evaluate(self, chromo):
        schedule = build_schedule(chromo, self.courses)
        reward, penalty = calculate_fitness(schedule, self.popularity)
        score = reward + penalty
        binary = chromo.binary_array(self.courses)
        return (chromo, binary, score)

    def process(self):
        pop = [self.evaluate(Chromosome(self.courses)) for _ in range(len(self.students))]
        gen = 0
        best = max(pop, key=lambda x: x[2])

        while best[2] < self.threshold:
            gen += 1
            selected = selection(pop)

            children = []
            while len(children) < len(selected):
                p1, _, _ = random.choice(selected)
                p2, _, _ = random.choice(selected)

                g1, g2 = crossover(
                    p1.binary_array(self.courses),
                    p2.binary_array(self.courses)
                )

                for g in [g1, g2]:
                    if len(children) >= len(selected):
                        break
                    child = Chromosome(self.courses)
                    bits = ''.join(map(str, g))
                    idx = 0
                    for c in self.courses:
                        child.genes[c["Course"]] = bits[idx:idx+3]
                        idx += 3
                    children.append(self.evaluate(child))

            next_gen = selection(children)
            if len(next_gen) != 10:
                raise Exception("Expected 10 individuals after offspring selection")

            mutated = []
            for chromo, binary, _ in next_gen:
                m_genes = mutation(binary)
                mutated_chromo = Chromosome(self.courses)
                bits = ''.join(map(str, m_genes))
                idx = 0
                for c in self.courses:
                    mutated_chromo.genes[c["Course"]] = bits[idx:idx+3]
                    idx += 3
                mutated.append(self.evaluate(mutated_chromo))

            pop = mutated
            current = max(pop, key=lambda x: x[2])
            if current[2] > best[2]:
                best = current

            print("Best fitness:", best[2])

        print("Fitness:", best[2])
        print("Gene:", best[1])

        best_chromo = best[0]
        schedule = build_schedule(best_chromo, self.courses)

        print("\nFinal Schedule:")
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for course, (day, slot) in schedule.items():
            print(f"{course}: {day_names[day]} {slot + 1}")

if __name__ == "__main__":
    Solution().process()