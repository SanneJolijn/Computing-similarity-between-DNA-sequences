#opening files with the interval lists
set1 = open('sample_set1.txt')
set2 = open('sample_set2.txt')

#reading in text files and putting them into lists
L1 = set1.readlines()
L2 = set2.readlines()

print(L1)

#we willen kijken of uit lijst 2 de intervals hun startnummer kleiner 
#zijn dan het eindnummer van de intervals uit lijst 1
