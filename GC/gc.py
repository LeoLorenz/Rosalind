"""Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below."""

with open('rosalind_gc.txt', 'r') as input_file:
    fasta = input_file.read().splitlines()
    gc_list, id_list, len_list = [], [], []
    for line in fasta:
        if ">" in line:
            id_list.append(line)
            gc_list.append(0)
            len_list.append(0)
        else:
            gc_list[-1] += (line.count("C") + line.count("G"))
            len_list[-1] += len(line)
for x in range(len(gc_list)):
    gc_list[x] = float(gc_list[x]/len_list[x])

max_gc = max(gc_list)
max_id = id_list[gc_list.index(max_gc)]
print(max_id[1:], "\n", round(max_gc*100, 6))
