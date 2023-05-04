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
intervalsL1 = [] #this is a list of tuples containing my intervals

#make usable lists of the lists of intervals of set 2
newL2 = []
for a in L2:
    new2 = ast.literal_eval(a)
    newL2.append(new2)
intervalsL2 = [] #this is a list of tuples containing my intervals


#trying the overlap code without using previous code
LS1 = [([2,5],[11,17],[22,37]), ([110,117],[255,263])]
LS2 = [([3,8],[18,20],[24,26],[29,33]), ([117,120],[240,256],[259,307])]

#for ls12
overlap_list = []
nr_intervals1 = []
nr_intervals2 = []
for tuple in LS1:
    overlap = 0
    intervals1 = 0
    for start1, end1 in tuple:
        intervals1 = intervals1 + 1
        for tuple2 in LS2:
            intervals2 = 0
            print(intervals2)
            for start2, end2 in tuple2:
                
                print(intervals2)
                if start1 <= end2 and end1 >= start2:
                    overlap = overlap + 1
                    break  # Exit the inner loop if overlap is found
    overlap_list.append(overlap)
    nr_intervals1.append(intervals1)
    nr_intervals2.append(intervals2)

print(overlap_list)
print(nr_intervals1)
print(nr_intervals2)

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


#n1 and n2 are the numbers of intervals in the lists