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
NUM_SLOTS_PER_DAY = 5

def parse_time(time_str):
    parts = time_str.strip().split()
    if len(parts) != 2:
        return None
    day_name, slot_str = parts
    if day_name not in DAYS:
        return None
    try:
        slot_number = int(slot_str)
        return DAYS[day_name], slot_number
    except ValueError:
        return None

def load_courses(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        courses = []
        for row in reader:
            if not row or len(row) < 2:
                continue
            course_name = row[0].strip()
            slots = []
            for value in row[1:]:
                parsed = parse_time(value)
                if parsed:
                    slots.append(parsed)
            courses.append({
                "Course": course_name,
                "Slots": slots
            })
        return courses

def load_students(path):
    students = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Student Name"]
            preferences = {}
            for time_str, score in row.items():
                if time_str == "Student Name" or not score.strip():
                    continue
                parsed = parse_time(time_str)
                if parsed:
                    preferences[parsed] = int(score)
            students.append({
                "name": name,
                "schedule": preferences
            })
    return students