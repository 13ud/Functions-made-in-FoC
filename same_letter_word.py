def same_letter_word(word1, word2):
    letters_freq = {}

    for letter1 in word1:
        if letter1 in letters_freq:
            letters_freq[letter1] += 1
        else:
            letters_freq[letter1] == 1

    for letter2 in word2:
        if letter2 in letters_freq:
            letters_freq[letter2] -= 1
        else:
            return False

    for letter in letters_freq:
        if letters_freq[letter] != 0:
            return False
    return True

print(same_letter_word('man', 'plan'))