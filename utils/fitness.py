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

def chromosome_to_schedule(chromosome,courses):
    len_arr = len(chromosome)

    result = []

    for i in range(0, len_arr - 3 + 1, 3):
        string = str(chromosome[i]) + str(chromosome[i + 1]) + str(chromosome[i + 2])
        dec = binary_to_decimal(string)
        course_index = i // 3
        tup = courses[course_index].get("Slots")[dec]
        result.append(tup)
    return result
        
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def calculate_fitness(schedule, popularity_data):
    reward = 0
    penalty = 0
    used_slots = set()
    day_slots = defaultdict(list)

    for (day, slot) in schedule:
        if (day, slot) in used_slots:
            return -1000
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
    point = reward + penalty
    return point