"""Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively."""

with open ('rosalind_ini4.txt', 'r') as input_file:
    limits = input_file.read()
    limits = limits.split(' ')
    result = 0
    for number in range (int(limits[0]), int(limits[1])):
        if number % 2 != 0:
            result += number
print(result)
