from utils.fitness import randomize_schedule, calculate_fitness, calculate_popularity
from utils.loader import load_courses, load_students, DAY_NAMES


class Solution:
    def __init__(
        self, courses_file="./data/courses.csv", students_file="./data/students.csv"
    ):
        self.courses_data = load_courses(courses_file)
        self.students_data = load_students(students_file)
        # TODO: Pre-process courses to convert time slots to (day, slot) tuples
        # self.courses = preprocess_courses(self.courses_data)
        self.popularity = calculate_popularity(self.students_data)

    def process(self):
        for student in self.students_data:
            # TODO: Implement the chromosome logic here
            schedule = randomize_schedule(self.courses_data)
            reward, penalty = calculate_fitness(schedule, self.popularity)
            total_score = reward + penalty

            print(f"\nSinh viên: {student['Student Name']}")
            print(f"Tổng điểm: {total_score} (Reward: {reward}, Penalty: {penalty})")
            print("Lịch học:")
            for course, (day, slot) in schedule.items():
                key = f"{DAY_NAMES[day]} {slot}"
                print(
                    f"  {course}: {DAY_NAMES[day]} {slot} "
                    f"(popularity: {self.popularity.get((day, slot), 0)}, "
                    f"preference: {student.get(key, '0')})"
                )
            print("---")


solution = Solution()
# Student 1,1,2,2,1,2,4,4,3,1,2,1,3,2,3,1,2,1,2,1,1,4,3,1,4
# TODO: { chormosome, schedule, fitness }

# solution.process()
