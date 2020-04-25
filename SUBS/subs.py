"""Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s."""

with open ('rosalind_subs.txt', 'r') as input_file:
    dna=input_file.read().splitlines()
    res = []
    for i in range((len(dna[0]))-len(dna[1])):
        if dna[0][i:(i+len(dna[1]))] == dna[1]:
            res.append(i+1)
print(res)
