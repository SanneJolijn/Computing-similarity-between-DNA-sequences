def file_to_tuples(file_name):
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def has_overlap(interval, comparison_list):
    return any(interval[0] <= comp[1] and interval[1] >= comp[0] for comp in comparison_list)

def similarity(set_1='sample_set1.txt', set_2='sample_set2.txt', outfile='similarityV4.txt'):
    LS1 = file_to_tuples(set_1)
    LS2 = file_to_tuples(set_2)

    LS12_list = [sum(has_overlap(interval1, LS2[n]) for interval1 in LS1[n]) / max(len(LS1[n]), len(LS2[n])) 
                 + sum(has_overlap(interval2, LS1[n]) for interval2 in LS2[n]) / max(len(LS1[n]), len(LS2[n])) 
                 for n in range(len(LS1))]

    S_fin = sum(LS12_list) / len(LS1)

    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(S_fin))

    return S_fin

similarity()