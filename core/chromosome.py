import random

class Chromosome:
    def __init__(self, courses):
        self.genes = self._create_genes(courses)

    def _create_genes(self, courses):
        genes = {}
        for course in courses:
            course_name = course.get("Course")
            slots = course.get("Slots", [])
            if not slots:
                continue
            random_index = random.randint(0, len(slots) - 1)
            binary = format(random_index, '03b')
            genes[course_name] = binary
        return genes
    
    def selection(population, tournament_size=2):
        selected = []
        for _ in range(len(population)):
            tournament = random.sample(population, tournament_size)
            winner = max(tournament, key=lambda x: x[1])
            selected.append(winner)

            selected.sort(key=lambda x: x[1], reverse=True)
            half = selected[:len(selected)//2]
        return half

    def binary_array(self, course_order):
        binary_str = ''.join(self.genes[course["Course"]] for course in course_order)
        return [int(bit) for bit in binary_str]
