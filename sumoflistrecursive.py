def sumoflist(my_list):
    if len(my_list) == 0:
        return f"The sum of elements in the list is: 0"

    if len(my_list) == 1:
        return my_list[0]

    else:
        return my_list[0] + sumoflist(my_list[1:])

print(sumoflist([1,2,3]))