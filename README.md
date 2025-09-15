# Evolution Simulation

This Python script (`evolution.py`) simulates the evolution of a creature's traits using a simple genetic algorithm. It models how three main properties—Intelligence, Strength, and Agility—evolve over generations to maximize a fitness score.

## Core Concepts

The simulation is based on the following components:

### Gene Properties
The creature's genetic makeup is represented by a list of three values:
- **Intelligence (I):** Affects the creature's learning and problem-solving abilities.
- **Strength (S):** Affects the creature's physical power.
- **Agility (A):** Affects the creature's speed and dexterity.

### Fitness Function
The `fitness_score` function determines how "good" a particular set of genes is. It calculates a score based on the benefits each gene provides, balanced against the energy cost required to maintain them. The goal of the evolution is to maximize this score.

### Cost Function
The `cost` function calculates the energy expenditure of a gene. Higher stats are more costly to maintain. The cost is subtracted from the total fitness score.

### Mutation
The `mutate` function introduces changes to the genes in each generation. It uses a gradient-based approach to intelligently guide the evolution towards a higher fitness score, while also adding a degree of randomness to explore new possibilities.

### Evolution
The `evolve` function runs the simulation for a specified number of generations. In each generation, the genes are mutated, and the new fitness score is calculated.

## How to Run

1.  **Prerequisites:** Make sure you have the required Python libraries installed:
    ```bash
    pip install torch numpy matplotlib
    ```

2.  **Execute the script:**
    ```bash
    python evolution.py
    ```

## Output

The script will:
1.  Print the initial gene and its fitness score to the console.
2.  Run the simulation for a large number of generations (default is 5,000,000), printing progress updates.
3.  Print the final evolved gene and its maximized fitness score.
4.  Display a `matplotlib` plot showing the progression of Intelligence, Strength, Agility, and the overall Fitness Score over the generations.

![Evolution Plot](output.png) 
*(Note: You will need to run the simulation to generate your own `output.png`)*
