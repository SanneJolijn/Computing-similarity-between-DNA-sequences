def file_to_tuples(file_name):
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

###
def binary_search_overlap(interval, comparison_list):
    left, right = 0, len(comparison_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if interval[0] <= comparison_list[mid][1] and interval[1] >= comparison_list[mid][0]:
            return True
        elif interval[0] > comparison_list[mid][1]:
            left = mid + 1
        else:
            right = mid - 1
    for i in range(left, len(comparison_list)):
        if interval[0] <= comparison_list[i][1] and interval[1] >= comparison_list[i][0]:
            return True
        elif interval[1] < comparison_list[i][0]:
            return False
    return False


def has_overlap(interval, comparison_list):
    left, right = 0, len(comparison_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if interval[0] <= comparison_list[mid][1] and interval[1] >= comparison_list[mid][0]:
            return 1
        elif interval[0] > comparison_list[mid][1]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

###

def similarity(set_1='sample_set0.txt', set_2='sample_set01.txt', outfile='similarity.txt'):
    LS1 = file_to_tuples(set_1)
    LS2 = file_to_tuples(set_2)

    S = 0
    for n in range(len(LS1)):
        n1, n2 = len(LS1[n]), len(LS2[n])
        ls12 = sum(binary_search()) / max(n1, n2)
        ls21 = sum(has_overlap(LS2[n][interval], LS1[n]) for interval in range(n2)) / max(n1, n2)
        LS12 = (ls12 + ls21) / 2
        S += LS12

    S_fin = S / len(LS1)

    with open(outfile, 'w') as x:
        x.write('%f' %S_fin)
        #x.write('%.2f' %S_fin)

    return S_fin

similarity()

###

def similarity(set_1='sample_set0.txt', set_2='sample_set01.txt', outfile='similarity.txt'):
    LS1 = file_to_tuples(set_1)
    LS2 = file_to_tuples(set_2)

    S = 0
    for n in range(len(LS1)):
        n1, n2 = len(LS1[n]), len(LS2[n])
        combined_intervals = sorted(LS1[n] + LS2[n])
        LS12 = sum(binary_search_overlap(interval, combined_intervals[i+1:]) for i, interval in enumerate(combined_intervals[:-1]) if interval[1] < combined_intervals[i+1][0])
        LS12 /= max(n1, n2)
        S += LS12

    S_fin = S / len(LS1)

    with open(outfile, 'w') as x:
        x.write('%f' %S_fin)

    return S_fin