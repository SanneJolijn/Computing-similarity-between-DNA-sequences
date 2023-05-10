def file_to_tuples(file_name):
    with open(file_name) as f:
        return [eval(line.strip()) for line in f]

def similarity(set_1='sample_set1.txt', set_2='sample_set2.txt', outfile='similarityV3.txt'):
    LS1 = list(file_to_tuples(set_1))
    LS2 = list(file_to_tuples(set_2))

    S = sum((sum(any(x[0] <= y[1] and x[1] >= y[0] for y in LS2[n]) for x in LS1[n]) + 
             sum(any(x[0] <= y[1] and x[1] >= y[0] for y in LS1[n]) for x in LS2[n])) / (len(LS1[n]) + len(LS2[n])) / 2
            for n in range(len(LS1))) / len(LS1)

    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(S))

    return S

similarity()
