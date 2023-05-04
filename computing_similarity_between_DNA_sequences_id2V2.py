import ast

#opening files with the interval lists
set1 = open('sample_set1.txt')
set2 = open('sample_set2.txt')

#reading in text files and putting them into lists
L1 = set1.readlines() #dit is een lijst van strings
L2 = set2.readlines() #dit is een lijst van strings

#make usable lists of the lists of intervals of set 1
LS1 = [] #this will be a list of tuples containing the interval lists, where one tuple is one line
for i in L1:
    new = ast.literal_eval(i)
    LS1.append(new)

print(LS1)

#make usable lists of the lists of intervals of set 2
LS2 = []
for a in L2:
    new2 = ast.literal_eval(a)
    LS2.append(new2)

print(LS2)

#trying the overlap code without using previous code
LS1D = [([2, 5], [11, 17], [22, 37]), ([110, 117], [255, 263]), ([44, 66], [87, 104], [188, 204]), ([2, 33], [47, 56], [90, 99], [301, 312], [554, 707])]
LS2D = [([3, 8], [18, 20], [24, 26], [29, 33]), ([117, 120], [240, 256], [259, 307]), ([20, 44], [71, 75], [180, 192], [303, 315]), ([7, 35], [45, 58], [101, 119], [1043, 1352])]

#for ls12
def has_overlap(l1, l2):
    overlap = 0
    for start1, end1 in l1:
        for start2, end2 in l2:
            if start1 <= end2 and end1 >= start2:
                 overlap = overlap + 1
                 break  # Exit the inner loop if overlap is found
    return overlap

results = []
for s in range(len(LS1D)):
    result = has_overlap(LS1D[s], LS2D[s])
    results.append(result)

print(results)


#for n1, n2 GAAT GOED!!
n1 = []
n2 = []
for tuple in LS1:
    n1.append(len(tuple))

for tuple2 in LS2:
    n2.append(len(tuple2))

#print('nr of intervals LS1', n1)
#print('nr of intervals LS2', n2)

