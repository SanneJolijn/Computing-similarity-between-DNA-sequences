from utils import read_file
from utils import has_overlap

def similarity(set_1, set_2, outfile):
    """Calculate the similarity metric between two data sets based on their interval lists.

    Args:
        set_1 (str): The name of the file containing the interval lists for the first data set.
        set_2 (str): The name of the file containing the interval lists for the second data set.
        outfile (str): The name of the file to create and store the final metric.

    Returns:

        The similarity metric portraying the similarity between the two data sets.

    Raises:
        IOError: If any of the input files cannot be opened or read.
        ValueError: If the content of any of the input files is not formatted correctly.

    """
    # Read interval lists from set_1 and set_2 files
    ls1 = read_file(set_1)
    ls2 = read_file(set_2)

    S_intermediate = 0
    for n in range(len(ls1)):
        n1, n2 = len(ls1[n]), len(ls2[n])
        # Calculate similarity metrics based on overlapping intervals
        ls12 = sum(has_overlap(ls1[n][interval], ls2[n]) for interval in range(n1)) / max(n1, n2)
        ls21 = sum(has_overlap(ls2[n][interval], ls1[n]) for interval in range(n2)) / max(n1, n2)
        LS = (ls12 + ls21) / 2
        S_intermediate += LS

    S = S_intermediate / len(ls1)

    # Write the similarity metric to the output file
    with open(outfile, 'w') as x:
        x.write('%.2f' % S)

    #this is a possible fix for the rounding to even nr https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
    #print(round((S+10**(-10)),2))
    #print(S)

    return S

#hij rond de getallen nog verkeerd af, en kijken hoe ik met het importeren of ik de meegegeven sets ook in mijn code die ik inlever wil definieren.
#ook kijken: zouden ze de de sets een verschillende hoeveelheid lines geven?