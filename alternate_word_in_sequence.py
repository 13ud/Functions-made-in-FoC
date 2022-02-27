def alternate(word):
    vowels = []
    consonants = []
    finalword = ''
    for letter in word:
        if letter in 'aeiou':
            vowels.append(letter)
        else:
            consonants.append(letter)

    if len(vowels) == len(consonants) - 1:
        finalword = consonants[0]
        for i in range(len(vowels)):
            finalword += vowels[i]
            finalword += consonants[i + 1]

        return finalword

    elif len(vowels) == len(consonants) + 1:
        finalword = vowels[0]
        for i in range(len(consonants)):
            finalword += consonants[i]
            finalword += vowels[i + 1]
        return finalword

    elif len(vowels) == len(consonants):
        finalword = sorted([vowels[0], consonants[0]])[0]
        if finalword in vowels:
            finalword += consonants[0]
            for i in range(len(consonants) - 1):
                finalword += vowels[i + 1]
                finalword += consonants[i + 1]
        else:
            finalword += vowels[0]
            for i in range(len(vowels) - 1):
                finalword += consonants[i + 1]
                finalword += vowels[i + 1]
        return finalword

    return None

print(alternate('tools'))
print(alternate('ambulance'))
print(alternate('headache'))
print(alternate('football'))



