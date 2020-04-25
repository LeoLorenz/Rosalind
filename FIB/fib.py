"""Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""


"""def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b"""

with open('rosalind_fib.txt', 'r') as input_file:
    values = input_file.read()
    values = values.split()
    for i in range (1, int(values[0])+1):
        if i == 1 :
            adult = 0
            offspring = 1
        elif i ==2:
            adult = 1
            offspring = 0
        else:
            new_adults = offspring
            offspring = adult * int(values[1])
            adult = adult + new_adults
print(int(adult + offspring))
