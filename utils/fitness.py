import random
from collections import defaultdict, Counter

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

def calculate_popularity(students):
    counter = Counter()
    for student in students:
        for time_slot, weight in student.items():
            if time_slot == "Student Name":
                continue
            day, slot = time_slot.split()
            counter[(DAYS[day], int(slot))] += int(weight)
    return counter

def random_schedule(courses):
    schedule = {}
    for course in courses:
        parsed = [parse_time(opt) for opt in course['Times']]
        schedule[course['Course']] = random.choice(parsed)
    return schedule

def fitness(schedule, student_row, popularity):
    penalty = 0
    reward = 0
    day_slots = defaultdict(list)
    seen = set()

    for course, (day, slot) in schedule.items():
        if (day, slot) in seen:
            return 0, -1000

        seen.add((day, slot))
        reward += popularity.get((day, slot), 0)
        day_slots[day].append(slot)

    if sum(len(day_slots[d]) for d in [4, 5]) > sum(len(day_slots[d]) for d in [0, 1, 2, 3]):
        penalty -= 50

    for slots in day_slots.values():
        slots = sorted(slots)
        if len(slots) >= 4:
            for i in range(len(slots) - 3):
                if slots[i:i+4] == [1, 2, 3, 4]:
                    penalty -= 150
                    break
    return reward, penalty