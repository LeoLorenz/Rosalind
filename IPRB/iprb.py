def mendel(x, y, z):
    #calculate the probability of recessive traits only
    total = x+y+z
    twoRecess = (z/total)*((z-1)/(total-1))
    twoHetero = (y/total)*((y-1)/(total-1))
    heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    print(1-recessProb) # take the complement

#mendel(2, 2, 2)

with open ("rosalind_iprb.txt", "r") as file:
    line =file.readline().split()
    x, y, z= [int(n) for n in line]
    print(x, y, z)
file.close()
print(mendel(x, y, z))
