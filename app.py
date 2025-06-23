from core.fitness import Solution, random_schedule, fitness, DAY_NAMES

solution = Solution()
courses = solution.courses_data
students = solution.students_data
popularity = solution.popularity

for student in students:
    sched = random_schedule(courses)
    reward, penalty = fitness(sched, student, popularity)
    total_score = reward + penalty

    print(f"\nSinh viên: {student['Student Name']}")
    print(f"Tổng điểm: {total_score} (Reward: {reward}, Penalty: {penalty})")
    print("Lịch học:")
    for course, (day, slot) in sched.items():
        key = f"{DAY_NAMES[day]} {slot}"
        print(f"  {course}: {DAY_NAMES[day]} {slot} (popularity: {popularity.get((day, slot), 0)}, preference: {student.get(key, '0')})")
    print("---")
