# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    m = [[] for i in range(n)]
    
    for i in range(n):

        if m2[i] == -1:

            m3 = 1

        else:

            m[m2[i]].append(i)


def depth(node):

    if not m[node]:
        
        return 1

    else:

        return max(depth(child) for child in m[node]) + 1

    m4 = [depth(mm) for mm in m[m3]]

    return max(m4)


def main():

    n = int(imput())

    m2 = list(map(int, input().split()))

    height = compute_height(n, m2)

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