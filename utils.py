def read_file(file_name):
    """
    Args:
        file_name (str): The name of the file containing 
                         the interval lists.

    Returns:
        A list of tuples containing intervals, 
        where each tuple corresponds to one line in the file.

    Raises:
        IOError: If the file cannot be opened or read.
        ValueError: If the content of the file
                    is not formatted correctly.
    """
    with open(file_name) as f:
        # Read each line in the file 
        # and format it as a tuple representing an interval.
        return [eval(line.strip()) for line in f]


def has_overlap(interval, to_compare):
    """Determine if there is an overlap between two intervals
       by comparing their start and end numbers.

    Args:
        interval (list): One interval to compare.
        to_compare (tuple): One tuple from the file 
                            you want to compare to.

    Returns:
        1 if overlap is found between intervals.
        0 if no overlap is found between intervals.
    
    Raises:
        TypeError: If either interval or to_compare
                   is not a list of tuples.
        ValueError: If either interval or any tuple in to_compare   
                    is not of length 2.

    """
    # Compare the interval against each interval
    # in the corresponding list of the other data set.
    for i in range(len(to_compare)):
        if (interval[0] <= to_compare[i][1] and 
            interval[1] >= to_compare[i][0]):
            return 1
    return 0

