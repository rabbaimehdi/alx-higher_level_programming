#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list."""
    sum = 0
    while True:
        try:
            if sum < x:
                print(my_list[sum], end='')
                sum += 1
            else:
                print()
                return sum
        except IndexError:
            print()
            return sum
