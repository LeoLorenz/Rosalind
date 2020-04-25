with open('rosalind_ini3.txt') as myfile:
    text = myfile.read()
    text_list = text.splitlines()
    limits = text_list[1].split(' ')
print(text_list[0][int(limits[0]):(int(limits[1])+1)]
        + ' ' +
        text_list[0][int(limits[2]):(int(limits[3])+1)])
