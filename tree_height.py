# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    tree = [[] for i in range(n)]
    
    for i in range(n):

        if parents[i] == -1:

            root = 1

        else:

            tree[parents[i]].append(i)


def depth(node, tree):

    if not tree[node]:
        
        return 1

    else:

        return max(depth(child, tree) for child in tree[node]) + 1


    return depth(root, tree)


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
main()
# print(numpy.array([1,2,3]))