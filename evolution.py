import torch
import random
import numpy as np
import matplotlib.pyplot as plt
import math

par = [0.6,0.5,0.2,0.1]

"""
gene properties:
- intelligence: affects learning speed
- strength: affects physical tasks
- agility: affects speed and dexterity
"""

gene = [0,0,1] # Intelligence, strength, agility

def cost(gene):
    I, S, A = gene
    Energy_cost = par[0] * I ** 1.5 + par[1] * S ** 2 + A * par[2] + par[3]
    return math.log10(max(Energy_cost,0.01))

def fitness_score(gene):
    I, S, A = gene
    IS = 50 / (1 + math.exp(-10 * (I - 1)))
    SS = 125 * (1 - math.exp(-3 * S))
    AS = 40 * math.log(1 + A * 10)
    return ((IS + SS + AS) - cost(gene)) * 100

def mutate(gene, mutation_rate=0.01):
    new_gene = []
    h = 1e-6
    i = 0
    for prop in gene:
        val = 0
        tmp = gene
        tmp[i] += h
        d = (fitness_score(tmp) - fitness_score(gene)) / h
        d *= mutation_rate
        val = prop + d + random.uniform(-mutation_rate, mutation_rate)
        new_gene.append(max(val, 0))
        i += 1
    return new_gene

def evolve(gene, generations=100):
    history = []
    for gen in range(int(generations)):
        gene = mutate(gene)
        score = fitness_score(gene)
        history.append(gene + [gen,score / 5000])
        if gen % 100 == 0:
            print(f"Generation {gen}: Gene {gene}, Fitness Score: {round(score)}")
    return gene, history
print("Initial gene:", gene, "Fitness Score:", round(fitness_score(gene)))
final_gene, history = evolve(gene, generations=5e6)
print("Final gene:", final_gene, "Fitness Score:", round(fitness_score(final_gene)))

I = [h[0] for h in history]
S = [h[1] for h in history]
A = [h[2] for h in history]
T = [h[3] for h in history]
SC = [h[4] for h in history]

plt.plot(T, I, label='Intelligence',color='red')
plt.plot(T, S, label='Strength',color='green')
plt.plot(T, A, label='Agility',color='blue')
plt.plot(T, SC, label='Fitness Score',color='black')
plt.xlabel('Generations')
plt.ylabel('Gene Value')
plt.show()





    


