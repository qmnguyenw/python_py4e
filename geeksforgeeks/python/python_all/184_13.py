Python Program to find largest element in an array



Given an array, find the largest element in it.

    
    
    Input : arr[] = {10, 20, 4}
    Output : 20
    
    Input : arr[] = {20, 10, 20, 4, 100}
    Output : 100
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find maximum

# in arr[] of size n 

 

# python function to find maximum

# in arr[] of size n

def largest(arr,n):

 

 # Initialize maximum element

 max = arr[0]

 

 # Traverse array elements from second

 # and compare every element with 

 # current max

 for i in range(1, n):

 if arr[i] > max:

 max = arr[i]

 return max

 

# Driver Code

arr = [10, 324, 45, 90, 9808]

n = len(arr)

Ans = largest(arr,n)

print ("Largest in given array is",Ans)

 

# This code is contributed by Smitha Dinesh Semwal  
  
---  
  
 __

 __

Please refer complete article onProgram to find largest element in an array
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

