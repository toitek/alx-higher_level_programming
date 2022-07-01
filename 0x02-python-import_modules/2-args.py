#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        i = 0
        for args in sys.args:
            if i != 0:
                print("{}: {}".format(i, args))
            i += 1
