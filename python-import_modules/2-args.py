#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argv_len = len(argv) - 1
if argv_len == 0:
    print("{} arguments".format(argv_len))
elif argv_len == 1:
    print("{} argument:".format(argv_len))
else:
    print("{} argument:".format(argv_len))
for i in range(argv_len):
    print("{}: {}".format(i + 1, argv[i + 1]))
