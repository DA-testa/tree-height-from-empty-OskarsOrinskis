# python3

import sys
import threading
import numpy


def compute_height(n, parents):
   
    tree = [[] for m in range(n)]
    
    for i in range(n):

        parnet = parents[i]

        if parent == -1:

            root

        else:

            tree[parent].append(i)


    a = stack

    a.appent(root)

    height = 0

    while a:

        size = len(a)

        for m in range(size):

            node = a.popleft()

            for child in children[node]:

                a.append(child)

        if a:

            height += 1

        return height

        

    while i != -1

        if heights[i] != 0:
            
            break

        heights[i] = height

        height -= 1

        i = parents[i]

    return max_height


  


def main():

    n = int input().strip()

    if input_type == 'I'

    r = int(input())

    nodes = list(map(int, input().split()))

    elif input_type == 'F'

    filename = input()

    with open(os.path.join("test", filename), 'r') as f:

        r = int(f.readline().strip())

        nodes = list(map(int, f.readline().split()))

    print(height)

    else:

    print("erorr")

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