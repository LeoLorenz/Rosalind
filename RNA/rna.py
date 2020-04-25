"""Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t."""

with open ('rosalind_rna.txt', 'r') as input_file:
    t = input_file.read()
print(t.replace("T", "U")
