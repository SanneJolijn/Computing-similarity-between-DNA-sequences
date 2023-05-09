#importing needed packages
import ast


def open_read_file(file_name):
    set1 = open(file_name) #opening files with the interval lists
    L1 = set1.readlines() #dit is een lijst van strings #reading in text files and putting them into lists
    LS1 = [] #make usable lists of the lists of intervals of set 1 #this will be a list of tuples containing the interval lists, where one tuple is one line
    for i in L1:
        new = ast.literal_eval(i)
        LS1.append(new)
    return LS1

LS1 = open_read_file('sample_set3.txt')
LS2 = open_read_file('sample_set4.txt')

#for computing similarity
def has_overlap(l1, l2):
    overlap = 0
    for start1, end1 in l1:
        for start2, end2 in l2:
            if start1 <= end2 and end1 >= start2:
                 overlap = overlap + 1
                 break  # Exit the inner loop if overlap is found
    return overlap

#for computing ls12 and ls21
def compute_ls_and_n(list_of_tuples):
    results_ls = []
    for s in range(len(list_of_tuples)):
        result = has_overlap(LS1[s], LS2[s])
        results_ls.append(result)

    n = []
    for tuple in list_of_tuples:
        n.append(len(tuple))
  
    return results_ls, n

results_12, n1 = compute_ls_and_n(LS1)
results_21, n2 = compute_ls_and_n(LS2)

#eventual calculations
def final_calculations(results1, results2, n1, n2, list_of_tuples):
    LStot = 0
    for s in range(len(results1)):
        ls12 = (results1[s]/max(n1[s],n2[s]))
        ls21 = (results2[s]/max(n1[s],n2[s]))
        LS = ((ls12 + ls21)/2)
        LStot = LStot + LS

    #since len(newL1) == len(newL2) always
    finalMetric = LStot / len(LS1)
    finalMetric_rounded = ('%.2f' %finalMetric)
    return finalMetric_rounded

fm_rounded = final_calculations(results_12, results_21, n1, n2, LS1)

print(fm_rounded)

#write result to file
#f = open("finalMetric.txt", "x")
#f.write(finalMetric_rounded)
