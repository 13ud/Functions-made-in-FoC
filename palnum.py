def twice(d):
    result = []
    i = 0
    while i < len(d):
        result = result + [d[i]] * 2
        i += 1
    return result

def palnum(num):
    biggest = 0
    for i in range(10 ** num, 10 ** (num + 1)):
        for j in range(10 ** num, 10 ** (num + 1)):
            product = i * j
            match = str(product) == str(product)[::-1]
            if match and product > biggest:
                biggest = product
    return biggest


print(palnum(1))

# line 1, syntax error. :
# line 8, runtime error. for point in trajectory
# line 16, runtime error. closestT = point[2]

print(float('inf'))
print(ord('z'))
