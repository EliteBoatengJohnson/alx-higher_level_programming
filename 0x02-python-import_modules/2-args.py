#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    1 = len(argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                 "." if l == 1 else ":"))
     for r, s in enumerate(argv):
        if r > 0:
            print("{:d}: {:s}".format(r, s))
