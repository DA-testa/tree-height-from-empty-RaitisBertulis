# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    heights = [0] * n

    for i in range(n):
        node_height = 0
        current = i
        while current != -1:
            if heights[current] != 0:
                node_height += heights[current]
                break
            node_height += 1
            current = parents[current]
        heights[i] = node_height
    return max(heights)



def main():
    # implement input form keyboard and from files
    cmd = input()
    if "I" in cmd:
        n=int(input())
        #parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    # let user input file name to use, don't allow file names with letter a
    elif "F" in cmd:
    # account for github input inprecision
        nos=input()
        if "a" not in nos:
            with open(f"test/{nos}") as f:
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
                n = int(f.readline().strip())
                parents=list(map(int, f.readline().strip().split()))
    # call the function and output it's result
    print(compute_height(n, parents))
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
