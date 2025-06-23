import csv

DAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5
}
DAY_NAMES = list(DAYS.keys())

def parse_time(time_str):
    day_str, slot = time_str.strip().split()
    return (DAYS[day_str], int(slot))

def load_courses(path):
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

def load_students(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]