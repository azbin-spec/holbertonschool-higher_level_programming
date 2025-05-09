#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if char > 96 and char < 123:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()
