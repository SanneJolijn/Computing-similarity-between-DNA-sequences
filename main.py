def file_to_tuples(file_name):
    """This function opens the provided files and reads into them.
    .....

    Args:
        file_name (str): The name of the file containing the interval lists.
    
    Returns:
        A list of tuples containing the intervals. Where each tuple is one line in the text file.

    """
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def has_overlap(interval, comparison_list):
    """.....

    Args:
        interval ():
        comparison_list ():

    Returns:
        1 when overlap is found
        0 when no overlap is found
    """
    for i in range(len(comparison_list)):
        if interval[0] <= comparison_list[i][1] and interval[1] >= comparison_list[i][0]:
            return 1
    return 0
### hier kunnen we ook de any statement gebruiken, maar is dit efficienter?

def similarity(set_1='sample_set1.txt', set_2='sample_set2.txt', outfile='similarity.txt'):
    """.....

    Args:
        set_1 ():
        set_2 ():
        outfile ():
    
    Returns:
        The metric portraying the similarity between the two data sets
    """
    LS1 = file_to_tuples(set_1)
    LS2 = file_to_tuples(set_2)

    S = 0
    for n in range(len(LS1)):
        n1, n2 = len(LS1[n]), len(LS2[n])
        ls12 = sum(has_overlap(LS1[n][interval], LS2[n]) for interval in range(n1)) / max(n1, n2)
        ls21 = sum(has_overlap(LS2[n][interval], LS1[n]) for interval in range(n2)) / max(n1, n2)
        LS12 = (ls12 + ls21) / 2
        S += LS12

    S_fin = S / len(LS1)

    with open(outfile, 'w') as x:
        x.write('%f' %S_fin)
        #x.write('%.2f' %S_fin)

    return S_fin

similarity()