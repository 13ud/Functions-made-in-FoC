def all_vowels(word):
    vowels = 'aeiou'
    seen = ''
    c = 0
    while c < len(word):
        if word[c] in vowels:
            seen += word[c]
        c += 1

    return sorted(seen) == list(vowels)

print(all_vowels('man'))


# Q3

# line 6, run time error. vote = []
# line 8, syntax error. current = candidates[i]
# line 10, syntax error. for o in orderings(remaining):