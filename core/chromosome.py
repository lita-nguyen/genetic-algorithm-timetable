import random

class Chromosome:
    def __init__(self, courses):
        self.genes = self._generate_genes(courses)

    def _generate_genes(self, courses):
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

    def __str__(self):
        return "\n".join(f"{course}: {binary}" for course, binary in self.genes.items())