Python Program for Activity Selection Problem | Greedy Algo-1



 _You are given n activities with their start and finish times. Select the
maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time._  
Example:

    
    
    **Example 1 :** Consider the following 3 activities sorted
    by finish time.
         start[]  =  {10, 12, 20};
         finish[] =  {20, 25, 30};
    A person can perform at most **two** activities. The 
    maximum set of activities that can be executed 
    is {0, 2} [ These are indexes in start[] and 
    finish[] ]
    
    **Example 2 :** Consider the following 6 activities 
    sorted by by finish time.
         start[]  =  {1, 3, 0, 5, 8, 5};
         finish[] =  {2, 4, 6, 7, 9, 9};
    A person can perform at most **four** activities. The 
    maximum set of activities that can be executed 
    is {0, 1, 3, 4} [ These are indexes in start[] and 
    finish[] ]
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

"""The following implementation assumes that the activities

are already sorted according to their finish time"""

 

"""Prints a maximum set of activities that can be done by a

single person, one at a time"""

# n --> Total number of activities

# s[]--> An array that contains start time of all activities

# f[] --> An array that contains finish time of all activities

 

def printMaxActivities(s, f ):

 n = len(f)

 print "The following activities are selected"

 

 # The first activity is always selected

 i = 0

 print i,

 

 # Consider rest of the activities

 for j in xrange(n):

 

 # If this activity has start time greater than

 # or equal to the finish time of previously

 # selected activity, then select it

 if s[j] >= f[i]:

 print j,

 i = j

 

# Driver program to test above function

s = [1, 3, 0, 5, 8, 5]

f = [2, 4, 6, 7, 9, 9]

printMaxActivities(s, f)

 

# This code is contributed by Nikhil Kumar Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    The following activities are selected
    0 1 3 4
    

Please refer complete article on Activity Selection Problem | Greedy Algo-1
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

