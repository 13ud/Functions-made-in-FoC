def remove_punct(word):
    punct = ''
    while word:
        if word[-1] in '.,!?':
            punct = word[-1] + punct
            word = word[:-1]
        else:
            break
    return word, punct

def shorten(text, MAXLEN=4):
    short_text = ''
    for word in text.split():
        word, punct = remove_punct(word)
        if len(word) > MAXLEN:
            word = word[:MAXLEN//2] + word[-MAXLEN//2:]
        short_text += word + punct + ' '
    return short_text[:-1]

print(shorten("In a hole in the ground there lived a hobbit."))
