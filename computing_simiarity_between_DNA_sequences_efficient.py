#import ast

def file_to_tuples(file_name):
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def has_overlap(l1, l2):
    overlap = 0
    for start1, end1 in l1:
        for start2, end2 in l2:
            if start1 <= end2 and end1 >= start2:
                 overlap = overlap + 1
                 break  # Exit the inner loop if overlap is found
    return overlap

def compute_ls_and_n(list_of_tuples):
    results_ls = []
    n = []
    for s, intervals in enumerate(list_of_tuples):
        result = has_overlap(intervals, list_of_tuples[s+1:])
        results_ls.append(result)
        n.append(len(intervals))
    return {'results': results_ls, 'n': n}

def final_calculations(results1, results2, n1, n2):
    LStot = 0
    num_sets = len(n1)
    for s in range(num_sets):
        ls12 = (results1[s]/max(n1[s],n2[s]))
        ls21 = (results2[s]/max(n1[s],n2[s]))
        LS = ((ls12 + ls21)/2)
        LStot += LS
    finalMetric = LStot / num_sets
    finalMetric_rounded = ('%.2f' %finalMetric)
    return finalMetric_rounded

###

def compute_overlap_and_n(list1, list2):
    overlaps = []
    n_values = []
    for t1, t2 in zip(list1, list2):
        overlap = 0
        n = max(len(t1), len(t2))
        for start1, end1 in t1:
            for start2, end2 in t2:
                if start1 <= end2 and end1 >= start2:
                    overlap += 1
                    break
        overlaps.append(overlap)
        n_values.append(n)
    return overlaps, n_values


def compute_final_metric(list1, list2):
    overlaps, n_values = compute_overlap_and_n(list1, list2)
    total_overlap = sum(overlaps) / sum(n_values)
    final_metric = total_overlap / len(list1)
    return round(final_metric, 2)


LS1 = file_to_list('sample_set3.txt')
LS2 = file_to_list('sample_set4.txt')

final_metric = compute_final_metric(LS1, LS2)
print(final_metric)