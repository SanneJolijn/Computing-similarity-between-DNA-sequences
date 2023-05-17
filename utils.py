def read_file(file_name):
    """Open and read a file containing interval lists, and format the content into a usable form.

    Args:
        file_name (str): The name of the file containing the interval lists.

    Returns:
        A list of tuples representing intervals, where each tuple corresponds to one line in the file.

    Raises:
        FileNotFoundError: [Errno 2] No such file or directory: 'sample_set.txt'
        IOError: If the file cannot be opened or read.
        ValueError: If the content of the file is not formatted correctly.

    """
    with open(file_name) as f:
        # Read each line in the file and format it as a tuple representing an interval
        return [eval(line.strip()) for line in f]


def has_overlap(interval, to_compare):
    """Determine if there is an overlap between two intervals by comparing their start and end numbers.

    Args:
        interval (tuple): One interval to compare.
        to_compare (tuple): One tuple from the file you want to compare to.

    Returns:
        1 if overlap is found between intervals.
        0 if no overlap is found between intervals.
    
    Raises:
        TypeError: If either interval or to_compare is not a list of tuples.
        ValueError: If either interval or any tuple in to_compare is not of length 2.

    """
    # Compare the interval against each interval in to_compare
    for i in range(len(to_compare)):
        if interval[0] <= to_compare[i][1] and interval[1] >= to_compare[i][0]:
            return 1
    return 0

### hier kunnen we ook de any statement gebruiken, maar is dit efficienter? En kan ik dit uitleggen in de docstring?

