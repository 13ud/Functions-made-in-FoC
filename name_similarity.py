def name_similarity(name1, name2, maxn=4):
    sim_list = []
    for n in range(2, maxn):
        if len(name1) >= n:
            matches = 0
            for start in range(0, len(name1) - (n - 1)):
                ngram = name1[start:start + n]
                if ngram in name2:
                    matches += 1
            sim_list.append(matches/(len(name1) - (n - 1)))

    if sim_list:
        return sum(sim_list)/len(sim_list)

    return 0.0


print(name_similarity('toto', 'totoro'))
print(name_similarity('tim', 'totoro'))
print(name_similarity('totoro', 'toto'))
print(name_similarity('', 'totoro'))