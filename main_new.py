def read_file(file_name):
    """Open and read a file containing interval lists, and format the content into a usable form.

    Args:
        file_name (str): The name of the file containing the interval lists.

    Returns:
        A list of tuples representing intervals, where each tuple corresponds to one line in the file.

    Raises:
        IOError: If the file cannot be opened or read.
        ValueError: If the content of the file is not formatted correctly.

    """
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]


def has_overlap(interval, to_compare):
    """Determine if there is an overlap between two intervals by comparing their start and end numbers.

    Args:
        interval (tuple): One interval to compare.
        to_compare (tuple): One tuple from the file you want to compare to.

    Returns:
        1 if overlap is found between intervals.
        0 if no overlap is found between intervals.

    """
    for i in range(len(to_compare)):
        if interval[0] <= to_compare[i][1] and interval[1] >= to_compare[i][0]:
            return 1
    return 0


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
        x.write('%f' % S)

    #this is a possible fix for the rounding to even nr https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
    print(round((S+10**(-10)),2))
    print(S)

    return S