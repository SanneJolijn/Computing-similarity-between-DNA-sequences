def read_file(file_name):
    """This function opens the provided files and reads into them. 
    It then formats the content of the file into a useable form

    Args:
        file_name (str): The name of the file containing the interval lists.
    
    Returns:
        A list of tuples containing the intervals. Where each tuple is one line in the text file.

    Raises:
        errors??

    """
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def has_overlap(interval, to_compare):
    """This function determines if there is overlap between two intervals by comparing the start and end numbers
       of both intervals. For every time the interval overlaps with one interval out of the to_compare tuple it returns a 1.

    Args:
        interval (lst): One interval out of the tuple you want to compare from.
        to_compare (tuple): One tuple from the file you want to compare to where the line number 
                            corresponds to the line number of line the interval originates from.

    Returns:
        1 when overlap is found between intervals.
        0 when no overlap is found between intervals.
    
    Raises:
        errors??
    """
    for i in range(len(to_compare)):
        if interval[0] <= to_compare[i][1] and interval[1] >= to_compare[i][0]:
            return 1
    return 0
### hier kunnen we ook de any statement gebruiken, maar is dit efficienter? En kan ik dit uitleggen in de docstring?

def similarity(set_1, set_2, outfile):
    """This function calls on the has_overlap function for every interval to compare it to the intervals in the tuple 
       from the corresponding line.

    Args:
        set_1 (str): The name of the file containing the interval lists. ##maar dit is nu gewoon hetzelfde als in de eerste functie
        set_2 (str): The name of the file containing the interval lists.
        outfile (str): The name of the file we create to put in our final metric.
    
    Returns:
        The metric portraying the similarity between the two data sets.
    
    Raises:
        errors??
    """
    ls1 = read_file(set_1)
    ls2 = read_file(set_2)

    S_intermediate = 0
    for n in range(len(ls1)):
        n1, n2 = len(ls1[n]), len(ls2[n])
        ls12 = sum(has_overlap(ls1[n][interval], ls2[n]) for interval in range(n1)) / max(n1, n2)
        ls21 = sum(has_overlap(ls2[n][interval], ls1[n]) for interval in range(n2)) / max(n1, n2)
        LS = (ls12 + ls21) / 2
        S_intermediate += LS

    S = S_intermediate / len(ls1)

    with open(outfile, 'w') as x:
        x.write('%f' %S)
        #x.write('%.2f' %S)

    return S

#hij rond de getallen nog verkeerd af, en kijken hoe ik met het importeren of ik de meegegeven sets ook in mijn code die ik inlever wil definieren.