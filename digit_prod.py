def digit_prod(num, start):
    seq = [start]
    for i in range(num):
        prod = 1
        cur = seq[-1]
        cur_str = str(cur)
        for digit in cur_str:
            digit = int(digit)
            if digit > 0:
                prod *= digit
        cur += prod
        seq.append(cur)
    return seq

print(digit_prod(15, 1))