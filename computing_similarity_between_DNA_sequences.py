import ast

#opening files with the interval lists
set1 = open('sample_set1.txt')
set2 = open('sample_set2.txt')

#reading in text files and putting them into lists
L1 = set1.readlines() #dit is een lijst van strings
L2 = set2.readlines() #dit is een lijst van strings


#we willen kijken of uit lijst 2 de intervals hun startnummer kleiner 
#zijn dan het eindnummer van de intervals uit lijst 1

#explanaition
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

#now we do the same for L2
newL2 = []

for a in L2:
    new2 = ast.literal_eval(a)
    newL2.append(new2)

intervalsL2 = [] #this is a list of tuples containing my intervals

for b in newL2:
    for c in b:
        intervalsL2.append(c)

#print(intervalsL2) #this is a list of my intervals as lists so this we can work with

beginL1 = []
endL1 = []

for x in intervalsL1:
    for y in range(0,1):
        beginL1.append(x[y])
    for z in range(1,2):
        endL1.append(x[z])

#print(beginL1)
#print(endL1)

#now do the same for L2
beginL2 = []
endL2 = []

for m in intervalsL2:
    for n in range(0,1):
        beginL2.append(m[n])
    for o in range(1,2):
        endL2.append(m[o])

#print(beginL2)
#print(endL2)

#now compare positions

overlap = 0

for d in range(len(beginL2)-2):
    if (endL1[d] > beginL2[d] > beginL1[d]) or (endL1[d] > endL2[d] > beginL1[d]):
        overlap = overlap + 1

print(overlap)

#now the same the other way around
overlap2 = 0

for e in range(len(beginL2)-2):
    if (endL2[e] > beginL1[e] > beginL2[e]) or (endL2[e] > endL1[e] > beginL2[e]):
        print('yes')
        overlap2 = overlap2 + 1

print(overlap2)

#nu proberen per interval lijstje van I langs L2 af te lopen en kijken of je er zo wel komt
#het probleem dat de code tegen verschillende lengtes aanloopt moet eruit want dat gaan ze sws testen