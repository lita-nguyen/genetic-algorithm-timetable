import random
from collections import defaultdict
from utils.loader import parse_time
from collections import Counter
from utils.loader import parse_time, DAYS, DAY_NAMES

def calculate_popularity(students):
    counter = Counter()
    for student in students:
        for time_slot, weight in student.items():
            if time_slot == "Student Name":
                continue
            key = parse_time(time_slot)
            counter[key] += int(weight)
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
        if len(slots) >= 3:
            for i in range(len(slots) - 2):
                if slots[i+2] - slots[i] == 2 and slots[i+1] - slots[i] == 1:
                    penalty -= 100
                    break
    return reward, penalty