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
max_key = []
cons = ""
res = [{"A" : 0, "T" : 0, "G" : 0, "C" : 0} for x in range(len(strands[0]))]
for i in range(len(strands[0])):
    for element in strands:
        if element[i] == "A":
            res[i]["A"] += 1
        elif element[i] == "C":
            res[i]["C"] += 1
        elif element[i] == "T":
            res[i]["T"] += 1
        elif element[i] == "G":
            res[i]["G"] += 1
    max_key =[k for k, v in res[i].items() if v == max(res[i].values())]
    cons += max_key[0]


print(cons, sep = "", end = "")
for base in ("A", "C", "G", "T"):
    print("\n")
    print(f"{base}:", end = "")
    for element in res:
        print(f"{element[base]}", end = "")
        
        
    
