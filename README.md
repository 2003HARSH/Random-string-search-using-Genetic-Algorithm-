# Random String Search Using Genetic Algorithm

This project demonstrates the use of a genetic algorithm to search for a target string. The algorithm evolves a population of random strings through selection, crossover, and mutation to progressively approximate the target string.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Classes and Methods](#classes-and-methods)
- [Output](#output)
- [Notes](#notes)
- [License](#license)

## Introduction

Genetic algorithms are a type of optimization algorithm inspired by the process of natural selection. This project uses a genetic algorithm to find a target string by evolving a population of candidate strings over multiple generations.

## Installation

To run the code, ensure you have Python installed. No additional libraries are required.

## Usage

The main components of this project are the `Dna` and `Population` classes. The `Dna` class defines the crossover and mutation methods, while the `Population` class manages the population of strings, calculates fitness scores, performs natural selection, and generates new populations.

### Classes and Methods

#### Dna Class

- **crossover(parent1, parent2)**: Combines two parent strings to create a child string.
- **mutation(child, mutation_rate)**: Applies mutations to the child string with a given mutation rate.

#### Population Class

- **\_\_init\_\_(target, population_size, mutation_rate)**: Initializes the population with the given target string, population size, and mutation rate.
- **generate_population()**: Generates an initial random population.
- **calculate_fitness(individual)**: Calculates the fitness of an individual string based on its similarity to the target string.
- **natural_selection()**: Selects the top individuals to form a mating pool.
- **generate_new_population()**: Generates a new population from the mating pool using crossover and mutation.

### Output

The code will print the best string found in each generation along with its fitness score. It will stop early if the target string is found.

![1](https://github.com/user-attachments/assets/4c799a59-93b2-4e03-ae81-3ef57bfec2f1)

## Notes

- The mutation rate controls the frequency of random changes in the strings.
- The fitness function measures the similarity of each string to the target string.
- The code can be adjusted to work with different target strings, population sizes, and mutation rates.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


