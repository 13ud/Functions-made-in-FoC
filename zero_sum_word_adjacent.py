def zero_sum_word(word):
    sum = 0
    for i in range(len(word) - 1):
        difference = ord(word[i+1]) - ord(word[i])
        sum += difference

    return sum == 0

print(zero_sum_word('pomp'))
print(zero_sum_word('disorder'))



