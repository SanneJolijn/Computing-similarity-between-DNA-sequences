def file_to_tuples(file_name):
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def has_overlap(interval, comparison_list):
    return any(interval[0] <= comp[1] and interval[1] >= comp[0] for comp in comparison_list)

def similarity(set_1='sample_set1.txt', set_2='sample_set2.txt', outfile='similarityV2.txt'):
    LS1 = file_to_tuples(set_1)
    LS2 = file_to_tuples(set_2)

    S = 0
    for n in range(len(LS1)):
        n1, n2 = len(LS1[n]), len(LS2[n])
        LS12 = (sum(has_overlap(LS1[n][interval], LS2[n]) for interval in range(n1)) / max(n1, n2)
               + sum(has_overlap(LS2[n][interval], LS1[n]) for interval in range(n2)) / max(n1, n2)) / 2
        S += LS12

    S_fin = S / len(LS1)

    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(S_fin))

    return S_fin

similarity()
