# Import the functions we need from our utils file.
from utils import (
    read_file,
    has_overlap
)


# Calculate the similarity metric.
def similarity(set_1, set_2, outfile):
    """Calculate the similarity metric between two data sets 
       based on their interval lists. It reads two text files 
       as input, each corresponding to a set of interval lists.

    Args:
        set_1 (str): 
                The name of the file containing
                the interval lists for the first data set.
                Each lists is in a separate line with the 
                intervals given as pairs of numbers 
                enclosed in square brackets and 
                separated by a comma. 
        set_2 (str): 
                The name of the file containing 
                the interval lists for the second data set.
                Each lists is in a separate line with the 
                intervals given as pairs of numbers 
                enclosed in square brackets and 
                separated by a comma.
        outfile (str): 
                The name of the file the function 
                creates to store the final metric.

    Returns:
        similarity_metric (float):
                A real number corresponding to the similarity 
                measure between the two data sets, rounded
                to two decimal places. This is always a 
                number between 0 and 1. 
                The similarity metric is also written to a .txt
                file formatted as a string.

    Raises:
        IOError: If any of the input files cannot be opened or read.
        ValueError: If the content of any of the input files
                    is not formatted correctly.

    """
    # Read and format the interval lists from set_1 and set_2 files.
    set1 = read_file(set_1)
    set2 = read_file(set_2)  
    
    total_list_similarities = 0
    for n in range(len(set1)):
        # Calculate the length of each list of intervals for both sets. 
        n1, n2 = len(set1[n]), len(set2[n])

        # Calculate the similarity of one interval lists to the other
        # interval list based on overlapping intervals.
        list_similarity_12 = (sum(has_overlap(set1[n][interval], set2[n]) 
                              for interval in range(n1)) 
                              / max(n1, n2))
        list_similarity_21 = (sum(has_overlap(set2[n][interval], set1[n]) 
                              for interval in range(n2)) 
                              / max(n1, n2))
        
        # Calculate the similarity per pair of interval lists
        # and add this number to the total list similarity.
        list_similarity = ((list_similarity_12 + list_similarity_21) 
                            / 2)
        total_list_similarities += list_similarity

    # Calculate the set similarity by dividing the total list similarity
    # with the length of the data set, the amount of lines in the file.
    set_similarity = (total_list_similarities 
                      / len(set1))
    
    # Making sure the numbers will round correctly by the rules.
    similarity_metric = (set_similarity 
                         + 10**(-2*6))
    
    # Write the similarity metric to the output file.
    with open(outfile, 'w') as x:
        x.write('%.2f' % similarity_metric)

    return similarity_metric
