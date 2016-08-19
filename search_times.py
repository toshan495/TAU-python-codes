def linear_search(my_list, x):
    ''' search for x in my_list '''
    for e in my_list:
        if e==x:
            return True

    return False  #if we got here the search failed

   
def binary_search(my_list, x):
    ''' search for x in my_list, which MUST BE SORTED !! '''
    left = 0
    right = len(my_list)-1

    while left<=right:
        mid = (left+right)//2
        if my_list[mid]==x:
            return True
        else:
            if my_list[mid] < x:    #go to right half
                left = mid+1
            else:                   #go to left half
                right = mid-1
    return False  #if we got here the search failed


############################################
## Time measurements
############################################
import time

for n in [10**5, 10**6, 10**7]:
    print("n=", n)

    L = [i for i in range(n)] #generates the list [0,1,2,...,n-1]

    t0 = time.clock()
    for i in range(100): #do 100 times, for more significant statistics
        linear_search(L,-1) #search a number that does not exist
    t1 = time.clock()
    print("sequential search:", t1-t0)

    t0 = time.clock()
    for i in range(100):  #do 100 times, for more significant statistics
        binary_search(L,-1) #search a number that does not exist
    t1 = time.clock()
    print("binary search:", t1-t0)
