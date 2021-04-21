Interesting Python Implementation for Next Greater Elements



Given an array, print the Next Greater Element (NGE) for every element. The
Next greater Element for an element x is the first greater element on the
right side of x in array. Elements for which no greater element exist,
consider next greater element as -1.

Examples:

    
    
    Input : 11, 13, 21, 3, 9, 12
    Output :
    11 --> 21
    13 --> 21
    21 --> -1
    3 --> 12
    9 --> 12
    12 --> -1
    
    Input : 10, 9, 8, 7, 6, 5, 4, 3, 2
    Output :
    10 --> -1
    9 --> -1
    8 --> -1
    7 --> -1
    6 --> -1
    5 --> -1
    4 --> -1
    3 --> -1
    2 --> -1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Below is a simple implementation in Python.

 __

 __  
 __

 __

 __  
 __  
 __

# Function for implementation of NGE

def NGE(arr):

 

 # Iterate through array to check for greatest element

 for i in range(0, len(arr)):

 

 # Find the maximum from i to end

 lead = max(arr[i:])

 

 # If max is same as the i'th number then 

 # print -1 else print the maximum

 if (arr[i] == lead):

 print("% d --> % d" % (arr[i], -1))

 else:

 print("% d --> % d" % (arr[i], lead))

 

 

# Driver program

def main():

 arr = [11, 13, 21, 3, 9, 12]

 NGE(arr)

 arr = [10, 9, 8, 7, 6, 5, 4, 3,
2]

 NGE(arr)

 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

Note that the time complexity of above solution is O(n*n). We can optimize it
inO(n) time using stack.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

