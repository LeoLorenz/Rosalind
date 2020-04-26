"""Given: Positive integers n≤100 and m≤20
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months."""
import itertools

with open ('rosalind_fibd.txt', 'r') as input_file:
    parameters = input_file.read().split()
    #[0] = end of simulation
    #[1] = life expectancy
    a = []
    for i in range(int(parameters[0])):
        a.append(itertools.repeat([0], int(parameters[0])))
    for month in range(parameters[0]):
        if month == 1:
            new_rab = 1
            adult_rab = 0
        elif month == 2:
            new_rab = 0
            adult_rab = 1
