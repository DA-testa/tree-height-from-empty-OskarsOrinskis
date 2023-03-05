# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    tree = [[] for i in range(n)]

    root = 0
    
    for i in range(n):


        if parent[i] == -1:

            root = 1

        else:

            tree[parent[i]].append(i)


    stack = [root]

    height = 0

    while stack:

        level_size = len(stack)


        for i in range(level_size):

            node = stack.pop(0)

            for child in tree[node]:

                stack.append(child)

        height += 1

    return height


  


def main():

    n = int(imput())

    parents = list(map(int, input().split()))

    height = compute_height(n, parents)

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