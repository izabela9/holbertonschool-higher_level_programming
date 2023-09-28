#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
result = 0
argv_len = len(argv)
if argv_len == 0:
    print("0")
for i in range(1, argv_len):
    result += int(argv[i])
print(result)
