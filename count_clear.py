def count_clear(state):
    countclear = len(state)
    for tStack in state:
        if tStack[1] != 'ground':
            countclear = countclear - 1
    return countclear

print(count_clear([['c1', 'c3'], ['c2', 'ground'], ['c3', 'ground']]))

print(count_clear([['c1', 'c3'], ['c3', 'c2'], ['c2', 'ground']]))
