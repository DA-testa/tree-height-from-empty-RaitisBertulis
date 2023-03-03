# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    for i in numpy.arange(n)
    skaits = 1
    sk = int(parents[i])
    while not (sk == -1):
        skaits = skaits + 1
        sk = int(parents[sk])
    max_height=max(max_height, skaits)
    return max_height


def main():
    # implement input form keyboard and from files
    cmd = input()
    if "I" in cmd:
        n=int(input())
        parents = input()
        mas=parents.split(" ")
        mas=numpy.array(mas)
        print(compute_height(n, mas))
    # let user input file name to use, don't allow file names with letter a
    elif "F" in cmd:
    # account for github input inprecision
        nos=input()
        path = "test/" + nos
        if not "a" in nos:
            with open(path, "t") as f:
                text=f.read()
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
                p = text.partition("\n")
                p1 = int(p[0])
                mas=p[2].split(" ")
                mas=numpy.array(mas)
    # call the function and output it's result
                print(compute_height(p1, mas))
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
