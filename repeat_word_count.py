def repeat_word_count(text, n):
    words = {}
    word_list = []
    for word in text.split():
        if word not in words:
            words[word] = 0
        words[word] += 1
    for word in words:
        if words[word] >= n:
            word_list.append(word)
    return(sorted(word_list))

print(repeat_word_count("buffalo buffalo buffalo buffalo", 2))

print(repeat_word_count("how much wood could a wood chuck chuck", 1))