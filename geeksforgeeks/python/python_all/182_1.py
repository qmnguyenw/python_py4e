Python Program for Range sum queries without updates



Given an array arr of integers of size n. We need to compute sum of elements
from index i to index j. The queries consisting of i and j index values will
be executed multiple times.

Examples:

    
    
    Input : arr[] = {1, 2, 3, 4, 5}
            i = 1, j = 3
            i = 2, j = 4
    Output :  9
             12         
    
    Input : arr[] = {1, 2, 3, 4, 5}
            i = 0, j = 4 
            i = 1, j = 2 
    Output : 15
              5
    

__

__  
__

__

__  
__  
__

# Python program to find sum between two indexes

# when there is no update.

 

def find_ans(ar, j, k):

 l = len(ar)

 for i in range(1, l):

 ar[i] = ar[i] + ar[i-1]

 

 print(ar[k] - ar[j-1])

 return; 

 

 

pr = [1, 2, 3, 4, 5]

ar = pr[:]

find_ans(ar, 1, 3)

ar = pr[:]

find_ans(ar, 2, 4)

 

# Code Contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    12
    

Please refer complete article on Range sum queries without updates for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

