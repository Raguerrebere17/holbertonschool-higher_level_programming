#!/usr/bin/python3
for x in range(00, 100):
    if (x < 10):
        print("0{}, ".format(x), end='')
    else:
        print("{}{}".format(x, (", " if x < 99 else "\n")), end='')
