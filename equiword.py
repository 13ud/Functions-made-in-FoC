from collections import defaultdict

def equiword(word):
    letters = list(word)
    frequency = defaultdict(int)
    for letter in letters:
        frequency[letter] += 1

    if len(set(list(frequency.values()))) != 1:
        return False

    return list(frequency.values())[0]


print(equiword("intestines"))
print(equiword("doggy"))