import re
import ast

#opening files with the interval lists
set1 = open('sample_set1.txt')
set2 = open('sample_set2.txt')

#reading in text files and putting them into lists
L1 = set1.readlines() #dit is een lijst van strings
L2 = set2.readlines() #dit is een lijst van strings


#we willen kijken of uit lijst 2 de intervals hun startnummer kleiner 
#zijn dan het eindnummer van de intervals uit lijst 1


#We first import the ast module, which provides a way to safely evaluate Python expressions as literals.
#We define a string string_with_lists containing a list of three sublists.
#We use ast.literal_eval() to safely evaluate the string as a Python literal. This function only evaluates literals such as strings, numbers, tuples, lists, dicts, booleans, and None, so it won't execute any arbitrary code.
#We assign the resulting list to list_of_lists.
#We print list_of_lists.

newL1 = []

for i in L1:
    new = ast.literal_eval(i)
    newL1.append(new)

intervalsL1 = [] #this is a list of tuples containing my intervals

for j in newL1:
    for k in j:
        intervalsL1.append(k)

print(intervalsL1) #this is a list of my intervals as lists so this we can work with