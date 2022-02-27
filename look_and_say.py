def look_and_say(prev):
    prev = str(prev)
    i = 0
    next_number = ''
    if len(prev) == 1:
        return int('1' + prev)

    while i <= len(prev) - 1:
        frequency = 1
        number = prev[i]
        while i < len(prev) - 1 and prev[i] == prev[i+1]:
            frequency += 1
            i += 1
        next_number += str(frequency) + str(number)
        i += 1
    return next_number

print(look_and_say(111221))

