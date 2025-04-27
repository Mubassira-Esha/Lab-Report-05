import random

def create_individual(n):
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_fitness(individual):
    n = len(individual)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if individual[i] == individual[j] or abs(individual[i]-individual[j]) == abs(i-j):
                conflicts += 1
    max_pairs = n*(n-1)//2
    return max_pairs - conflicts

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n-1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual, mutation_rate=0.1):
    n = len(individual)
    if random.random() < mutation_rate:
        idx = random.randint(0, n-1)
        individual[idx] = random.randint(0, n-1)
    return individual

def genetic_algorithm(n, population_size, generations):
    population = [create_individual(n) for _ in range(population_size)]

    for gen in range(generations):
        population = sorted(population, key=lambda ind: -calculate_fitness(ind))
        
        best = population[0]
        best_fitness = calculate_fitness(best)

        print(f"Generation {gen}: Best fitness = {best_fitness}")

        if best_fitness == n*(n-1)//2:
            print("Perfect solution found!")
            return best

        new_population = population[:2]
        while len(new_population) < population_size:
            parent1 = random.choice(population[:10])
            parent2 = random.choice(population[:10])
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return population[0]

if __name__ == "__main__":
    N = int(input("Enter the value of N for N-Queens: "))
    population_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))

    solution = genetic_algorithm(N, population_size, generations)

    print("\nFinal Solution Board (queen positions in each column):")
    print(solution)
    print("\nNOTE: Each index is a column, and the value is the row where the queen is placed.")
