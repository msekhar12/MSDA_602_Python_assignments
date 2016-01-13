import timeit
setup = '''
import numpy as np
import numpy.random as npr
import copy

import random

def sortwithloops(L):
   #Using bubble sort
 k = 0
 L_len = len(L)
 while (k <= L_len):  
   for i in range(L_len - k - 1):
        if(L[i] >= L[i+1]):
           temp = L[i]
           L[i] = L[i+1]
           L[i+1] = temp
   k = k + 1
 return(L)
   

def sortwithnumpy(arr):
    return(np.sort(arr))

def searchwithnumpy(arr, e):
    #return(any(arr == e))
    return(len(np.where(arr == e)[0]) > 0)


def sortwithoutloops(L):
 #  Using list.sort() to sort the input list
 L.sort()
 return(L)

def searchwithloops(L, x):
    #      Search a list's element using loop(s).
    #      Searches first occurrance and returns True if the element is found.

    for i in range(len(L)):
        if(L[i] == x):
           return(True)

    return(False)
    

def searchwithoutloops(L, x):
    #      searching a list with "in" operator
    return(x in L)

#Generate an array of 1000 elements from 0 to 999
numpyarr = np.random.permutation(np.arange(1000))[:]
L = numpyarr.tolist()

#Get a random number in the range 0 to 2000, and search for this value:
r = random.randrange(0,2000)

'''

if __name__ == "__main__":	

    n = 100
    t = timeit.Timer("x = copy.copy(L); sortwithloops(x)", setup = setup)
    print "sortwithloops:      ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(L); sortwithoutloops(x)", setup = setup)
    print "sortwithoutloops:   ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(numpyarr); sortwithnumpy(x)", setup = setup)
    print "sortwithnumpy:      ", t.timeit(n), " seconds"


    t = timeit.Timer("x=copy.copy(L); y = copy.copy(r); searchwithloops(x,y)", setup = setup)
    print "searchwithloops:    ", t.timeit(n), " seconds"

    t = timeit.Timer("x=copy.copy(L); y = copy.copy(r); searchwithoutloops(x,y)", setup = setup)
    print "searchwithoutloops: ", t.timeit(n), " seconds"
    
    t = timeit.Timer("x=copy.copy(numpyarr); y = copy.copy(r); searchwithnumpy(x,y)", setup = setup)
    print "searchwithnumpy:    ", t.timeit(n), " seconds"



