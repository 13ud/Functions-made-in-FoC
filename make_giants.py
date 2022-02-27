print(['ex-', 1][0].upper() + 'Soldier')
print(False or {'A': 2}['A'] % 2 in [1])
print(int('420'[0:2]) + 0)
print(len([]) + [7.0].pop(0))
print(sorted(list({'bar': 10, 'z': 1}.keys()))[0])

def make_giants(pack):
    doginfolist, doglist, finallist  = [], [], []
    for dogtuple in pack:
        if dogtuple[0] not in doglist:
            doginfolist.append([dogtuple])
            doglist.append(dogtuple[0])
        else:
            breedlistindex = doglist.index(dogtuple[0])
            doginfolist[breedlistindex].append(dogtuple)
    for lst in doginfolist:
        breed = lst[0][0]
        dplist = [dog[1] for dog in lst]
        hplist = [dog[2] for dog in lst]
        finallist.append((breed, sum(dplist), max(hplist)))
    return sorted(finallist)

print(make_giants([("husky", 2, 3), ("golden", 2, 2), ("husky", 1, 1), ("corgi", 1, 1)]))