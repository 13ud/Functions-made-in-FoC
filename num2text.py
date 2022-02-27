def num2txt(num, k=3):
    numstr = str(num)
    txt = ""
    mismatch = len(numstr) % k
    if mismatch:
        numstr = "0" * (k - mismatch) + numstr
    start = 0
    for end in range(k, len(numstr)+1, k):
        txt += chr(int(numstr[start:end]))
        start = end
    return txt


print(num2txt(97097114103104))

# line 9 syntax error start:end
# line 7 logic error start = 0
# line 4 logic error?, convert numstr back to int to divide. len(numstr)