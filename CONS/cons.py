"""Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)"""

with open ('rosalind_cons.txt', 'r') as input_file:
    text = input_file.read()
    strands = [[] for x in range(text.count('>'))]
    cont = 0
    text = text.splitlines()
    EMPTY = True
    a, c, g, t = "","","",""
    for line in text:
        if line.startswith(">"):
            if EMPTY == False:
                cont += 1
            else:
                EMPTY = False
            strands[cont] = ""
        else:
            strands[cont] += line

for element in strands:
    for i in range(len(strands[0])):
        a[i]+= (element[i].count("A"))
        c[i]+= (element[i].count("C"))
        g[i]+= (element[i].count("G"))
        t[i]+= (element[i].count("T"))
        


for i in range(len(strands[0])):
    for element in strands:
        a[i]+= (element[i].count("A"))
        c[i]+= (element[i].count("C"))
        g[i]+= (element[i].count("G"))
        t[i]+= (element[i].count("T"))
        
