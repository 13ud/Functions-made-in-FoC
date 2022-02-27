def valid_staffid(s_id):
    assert len(s_id) >= 5

    if not s_id[0].isdigit() > 0:
        return False

    special_chars = list("?!.@#_")
    for char in s_id[1:-4]:
        if char in special_chars:
            special_chars.remove(char)
        else:
            return False

    try:
        year = int(s_id[-4:])
        return year % 400 == 0 or (year % 100 != 0 and 4 == 0)
    except:
        return False

print(valid_staffid('12004'))
