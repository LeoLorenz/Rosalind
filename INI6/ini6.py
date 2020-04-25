"""Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order."""

with open ('rosalind_ini6.txt', 'r') as input_file:
    text_string = input_file.read()
    text_string = text_string.split(' ')
    dict = {}
    for word in text_string:
        if word not in dict:
            dict[word] = text_string.count(word)

for key, value in dict.items():
    print (key, " ", value)
