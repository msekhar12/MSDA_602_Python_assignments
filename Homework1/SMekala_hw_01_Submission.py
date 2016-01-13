def sortwithloops(L):
 '''
   Using bubble sort
 '''
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
   

def sortwithoutloops(L):
 '''
   Using list.sort() to sort the input list
 '''
 L.sort()
 return(L)

def searchwithloops(L, x):
    '''
      Search a list's element using loop(s).
      Searches first occurrance and returns True if the element is found.
    '''

    for i in range(len(L)):
        if(L[i] == x):
           return(True)

    return(False)
    

def searchwithoutloops(L, x):
    '''
      searching a list with "in" operator
    '''
    return(x in L)



if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
    
