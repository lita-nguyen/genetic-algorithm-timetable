import csv
from .fitness import calculate_popularity

class Solution: 
    def __init__(self, courses_file="./data/courses.csv", students_file="./data/students.csv"):
        self.courses_data = self.load_courses(courses_file)
        self.students_data = self.load_students(students_file)
        self.popularity = calculate_popularity(self.students_data)

    def load_courses(self, path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [
                {
                    'Course': row['Course'],
                    'Lecturer': row['Lecturer'],
                    'Times': [v.strip() for k, v in row.items() if k.startswith('Slot') and v.strip()]
                }
                for row in reader
            ]

    def load_students(self, path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]