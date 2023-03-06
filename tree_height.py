# python3

import sys
import threading
import numpy


def compute_height(parents):
   
    n = len(parents)

    heights = [0] * n

    max_height = 0
    
    for stack in range(n):


        if heughts[stack] != 0:

            continue

        else:

            tree[parent[i]].append(i)


    i= stack

    height = 0

    while i != -1:

        if heights[i] != 0:

            height += heights[i]

            break

        height += 1

        i = parents[i]

    max_height = max(max_height, height)

    i = stack

    while i != -1

        if heights[i] != 0:
            
            break

        heights[i] = height

        height -= 1

        i = parents[i]

    return max_height


  


def main():

    n = int input().strip()

    a = list(map(int, input().strip().split()))

    height = compute_height(parents)

    print(height)

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# print(numpy.array([1,2,3]))