#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        idx = 0
        for j in i:
            if idx != len(i) - 1:
                print("{:d}".format(j), end=" ")
                idx += 1
            else:
                print("{:d}".format(j), end="")
        print("")
