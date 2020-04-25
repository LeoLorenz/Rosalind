"""Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines."""

with open ('rosalind_ini5.txt', 'r') as myfile:
    mytext = myfile.read()
    mytext = mytext.splitlines()
    for i in range(len(mytext)):
        if i % 2 != 0:
            print(mytext[i])
