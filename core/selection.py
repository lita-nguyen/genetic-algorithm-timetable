import random

def selection(population, tournament_size=2):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda x: x[1])
        selected.append(winner)

        selected.sort(key=lambda x: x[1], reverse=True)
        half = selected[:len(selected)//2]
    return half