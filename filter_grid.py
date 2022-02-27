def filter_grid(grid, vals_to_replace):
    new_grid = []
    for row in grid:
        new_row = []
        for elem in row:
            new_elem = elem
            if elem in vals_to_replace:
                if len(new_row) == 0:
                    avg_before = 0
                else:
                    avg_before = int(sum(new_row) / len(new_row))
                new_elem = max(avg_before, elem)
            new_row.append(new_elem)
        if sum(new_row) % 2 == 0:
            new_grid.append(new_row)
    return new_grid

grid1 = [[3, 2], [3, 3, 2]]
grid2 = [[1, 2, 3], [4, 5, 6, 1]]
grid3 = [[10, 1, 4], [3, 6, 4, 1]]

print(filter_grid(grid1, [2]))
print(filter_grid(grid1, [3]))
print(filter_grid(grid2, [1, 2, 3, 4, 5, 6]))
print(filter_grid(grid3, [4]))
print(filter_grid(grid3, [1,4]))



