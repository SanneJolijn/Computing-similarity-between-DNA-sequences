# Importing all packages we need.
import ast


def file_to_list(file_name):
    '''This function opens the provided files and reads into them.
    The function then creates a list of strings containing the intervals.
    Since we cannot use the strings we convert these to lists of tuples containing the intervals.

    Args:
        file_name (str): The name of the file containing the interval lists.
    
    Returns:
        A list of tuples containing the intervals. Where each tuple is one line in the text file.

    '''
    openFile = open(file_name) 
    readFile = openFile.readlines() 

    listSimilarity = [] 
    for i in readFile:
        tupleSimilarity = ast.literal_eval(i)
        listSimilarity.append(tupleSimilarity)

    return listSimilarity

lS1 = file_to_list('sample_set3.txt')
lS2 = file_to_list('sample_set4.txt')


def has_overlap(l1, l2):
    overlap = 0
    for start1, end1 in l1:
        for start2, end2 in l2:
            if start1 <= end2 and end1 >= start2:
                 overlap = overlap + 1
                 break  # Exit the inner loop if overlap is found
    return overlap

#for computing ls12 and ls21
def compute_ls_n(list_of_tuples):
    results_ls = []
    for s in range(len(list_of_tuples)):
        result = has_overlap(lS1[s], lS2[s])
        results_ls.append(result)

    n = []
    for tuple in list_of_tuples:
        n.append(len(tuple))
  
    return results_ls, n

results_12, n1 = compute_ls_n(lS1)
results_21, n2 = compute_ls_n(lS2)

#eventual calculations
def final_calculations(results1, results2, n1, n2, list_of_tuples):
    LStot = 0
    for s in range(len(results1)):
        ls12 = (results1[s]/max(n1[s],n2[s]))
        ls21 = (results2[s]/max(n1[s],n2[s]))
        LS = ((ls12 + ls21)/2)
        LStot = LStot + LS

    #since len(newL1) == len(newL2) always
    finalMetric = LStot / len(lS1)
    finalMetric_rounded = ('%.2f' %finalMetric)
    return finalMetric_rounded

fm_rounded = final_calculations(results_12, results_21, n1, n2, lS1)

print(fm_rounded)
#write result to file
#f = open("finalMetric.txt", "x")
#f.write(finalMetric_rounded)
