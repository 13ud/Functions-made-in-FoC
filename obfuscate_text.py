

def obfuscate_text(text):
    subs = {'a': '@', 's': '$', 'i': '!', 'e': '3', 'l': '1'}

    obs_text = ''
    short_text = ''
    prev_char = ''
    i = 0

    for c in text:
        if c == prev_char:
            continue
        short_text += c
        prev_char = c

    while i < len(short_text):
        if short_text[i] in subs:
            obs_text += subs[short_text[i]]
        elif i % 2 == 0:
            obs_text += short_text[i].upper()
        else:
            obs_text += short_text[i]
        i += 1

    return obs_text

print(obfuscate_text('keeping secrets is wise'))