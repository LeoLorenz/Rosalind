"""Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)."""

with open ("rosalind_hamm.txt", "r") as input_file:
    dna = input_file.read().splitlines()
    diff = 0
    for i in range(len(dna[0])):
        if dna[0][i] != dna[1][i]:
            diff +=1
print(diff)
