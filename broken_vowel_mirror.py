def broken_vowel_mirror(word):
    if word == '':
        return 'Nothing to mirror'
    mirrored = ''
    i = len(word) - 1
    while i > (len(word) // 2):
        if word[i] in 'AEIOUaeiou':
            mirrored += word[i]
        i -= 1
    return mirrored

print(broken_vowel_mirror('racecar'))