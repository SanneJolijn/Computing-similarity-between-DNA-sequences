import ast

#opening files with the interval lists
set1 = open('sample_set3.txt')
set2 = open('sample_set4.txt')

#reading in text files and putting them into lists
L1 = set1.readlines() #dit is een lijst van strings
L2 = set2.readlines() #dit is een lijst van strings

#make usable lists of the lists of intervals of set 1
LS1 = [] #this will be a list of tuples containing the interval lists, where one tuple is one line
for i in L1:
    new = ast.literal_eval(i)
    LS1.append(new)

#print(LS1)

#make usable lists of the lists of intervals of set 2
LS2 = []
for a in L2:
    new2 = ast.literal_eval(a)
    LS2.append(new2)

#print(LS2)

#for computing similarity
def has_overlap(l1, l2):
    overlap = 0
    for start1, end1 in l1:
        for start2, end2 in l2:
            if start1 <= end2 and end1 >= start2:
                 overlap = overlap + 1
                 break  # Exit the inner loop if overlap is found
    return overlap

#for ls12
results_12 = []
for s in range(len(LS1)):
    result = has_overlap(LS1[s], LS2[s])
    results_12.append(result)
print('overlap from LS1 view', results_12)

#for ls21
results_21 = []
for s in range(len(LS2)):
    result = has_overlap(LS2[s], LS1[s])
    results_21.append(result)
print('overlap from LS2 view', results_21)

#for n1, n2 GAAT GOED!!
n1 = []
n2 = []
for tuple in LS1:
    n1.append(len(tuple))

for tuple2 in LS2:
    n2.append(len(tuple2))

print('nr of intervals LS1', n1)
print('nr of intervals LS2', n2)

#eventual formulas
LStot = 0
for s in range(len(results_12)):
    ls12 = (results_12[s]/max(n1[s],n2[s]))
    ls21 = (results_21[s]/max(n1[s],n2[s]))
    #print(ls12)
    #print(ls21)
    LS = ((ls12 + ls21)/2)
    #print(LS)
    LStot = LStot + LS

#since len(newL1) == len(newL2) always
finalMetric = LStot / len(LS1)
print(finalMetric)

#write result to file
#f = open("finalMetric.txt", "x")
finalMetric_rounded = ('%.2f' %finalMetric)
print(finalMetric_rounded)
#f.write(finalMetric_rounded)