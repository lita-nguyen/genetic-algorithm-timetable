import random
from collections import defaultdict, Counter
from utils.loader import parse_time

WEEKDAYS = [0, 1, 2, 3] 
WEEKENDS = [4, 5]    

def calculate_popularity(student_data):
    popularity_counter = Counter()
    for student in student_data:
        for time_slot, weight in student["schedule"].items():
            popularity_counter[time_slot] += int(weight)
    return popularity_counter

def build_schedule(chromosome, courses):
    schedule = {}
    for course in courses:
        course_name = course["Course"]
        binary = chromosome.genes.get(course_name)
        if binary is None:
            continue

        slot_index = int(binary, 2)
        available_slots = course["Slots"]

        if 0 <= slot_index < len(available_slots):
            schedule[course_name] = available_slots[slot_index]
        else:
            schedule[course_name] = random.choice(available_slots)
    return schedule

def calculate_fitness(schedule, popularity_data):
    reward = 0
    penalty = 0
    used_slots = set()
    day_slots = defaultdict(list)

    for course, (day, slot) in schedule.items():
        if (day, slot) in used_slots:
            return 0, -1000
        used_slots.add((day, slot))
        reward += popularity_data.get((day, slot), 0)
        day_slots[day].append(slot)

    weekday_count = sum(len(day_slots[d]) for d in WEEKDAYS)
    weekend_count = sum(len(day_slots[d]) for d in WEEKENDS)
    if weekend_count > weekday_count:
        penalty -= 50

    for slots in day_slots.values():
        slots.sort()
        for i in range(len(slots) - 2):
            if slots[i+1] == slots[i] + 1 and slots[i+2] == slots[i] + 2:
                penalty -= 100
                break
    return reward, penalty