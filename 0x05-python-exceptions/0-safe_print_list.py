#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list."""
    sum = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            sum += 1
        except:
            break
    print()
    return(sum)
