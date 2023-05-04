import ast

#opening files with the interval lists
set1 = open('sample_set1.txt')
set2 = open('sample_set2.txt')

#reading in text files and putting them into lists
L1 = set1.readlines() #dit is een lijst van strings
L2 = set2.readlines() #dit is een lijst van strings

#make usable lists of the lists of intervals of set 1
newL1 = [] #this will be a list of tuples containing the interval lists, where one tuple is one line
for i in L1:
    new = ast.literal_eval(i)
    newL1.append(new)



#make usable lists of the lists of intervals of set 2
newL2 = []
for a in L2:
    new2 = ast.literal_eval(a)
    newL2.append(new2)


#trying the overlap code without using previous code
LS1 = [([2,5],[11,17],[22,37])]
LS2 = [([3,8],[18,20],[24,26],[29,33])]

#for ls12
overlap_list = []
for tuple in LS1:
    overlap = 0
    for start1, end1 in tuple:
        for tuple2 in LS2:
            for start2, end2 in tuple2:
                if start1 <= end2 and end1 >= start2:
                    overlap = overlap + 1
                    break  # Exit the inner loop if overlap is found
    overlap_list.append(overlap)
print('overlap from LS1 view', overlap_list)

#for ls21
overlap_list2 = []
for tuple2 in LS2:
    overlap2 = 0
    intervals = 0
    for start2, end2 in tuple2:
        intervals = intervals + 1
        for tuple in LS1:
            for start1, end1 in tuple:
                if start2 <= end1 and end2 >= start1:
                    overlap2 = overlap2 + 1
                    break  # Exit the inner loop if overlap is found
    overlap_list2.append(overlap2)

print('overlap from LS2 view', overlap_list2)
#n1 and n2 are the numbers of intervals in the lists

#for n1, n2
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
for s in range(len(overlap_list)):
    ls12 = (overlap_list[s]/max(n1[s],n2[s]))
    ls21 = (overlap_list2[s]/max(n1[s],n2[s]))
    LS = ((ls12 + ls21)/2)
    LStot = LStot + LS

#since len(newL1) == len(newL2) always
finalMetric = LStot / len(newL1)

#write result to file
#f = open("finalMetric.txt", "x")
finalMetric_rounded = ('%.2f' %finalMetric)
#f.write(finalMetric_rounded)
