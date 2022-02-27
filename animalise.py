
def animalise(text, afile, newword="animal"):
    adict = {}
    out = ''
    with open(afile) as f:
        for line in f:
            adict[line.strip()] = True
    for word in text.split():
        if word in adict:
            out += newword + " "
        else:
            out += word + " "
    return out[:-1]

orig = "bear with me as I fix the bug in my python code"
print(animalise(orig, "animal-names.txt"))


