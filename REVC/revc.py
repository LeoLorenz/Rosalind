"""Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s."""


"""st = "AAAACCCGGT"
st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print st"""

with open('rosalind_revc.txt', 'r') as input_file:
    s = input_file.read()
    s = s[::-1]
    sc = ""
    for base in s:
        if base == "A":
            sc += "T"
        elif base == "T":
            sc += "A"
        elif base == "C":
            sc += "G"
        elif base == "G":
            sc += "C"
print(sc)
