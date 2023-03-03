# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    max_height = 0
    height = [0] * n
    for i in range(n):
        height2 = 0
        j= i
        while j != -1:
            if height[j] != 0:
                height2 = height2 + height[j]
                break
            height2 = 1 + height2
            j = parents[j]
        max_height=max(max_height, height2)
        k = i
        while k != -1 and height[k]==0:
            heigth[k] = height2
            heigth2 = heigth2 - 1
            k = parents[k]
    return max(max_height)

def main():
    cmd = input()
    if "F" in cmd:
        nos = input()
        if "a" not in nos:
            with open(f"test/{nos}") as file:
                n = int(file.readline().strip())
                parents=list(map(int, file.readline().strip().split()))
                print(compute_height(n, parents))
    elif "I" in cmd:
        n=int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
        
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
