#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    prints = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            prints += 1
        except:
            pass
    print()
    return prints
