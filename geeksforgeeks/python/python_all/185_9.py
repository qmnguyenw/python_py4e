Python Program for Counting Sort



Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of
hashing). Then doing some arithmetic to calculate the position of each object
in the output sequence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for counting sort

 

# The main function that sort the given string arr[] in 

# alphabetical order

def countSort(arr):

 

 # The output character array that will have sorted arr

 output = [0 for i in range(256)]

 

 # Create a count array to store count of inidividul

 # characters and initialize count array as 0

 count = [0 for i in range(256)]

 

 # For storing the resulting answer since the 

 # string is immutable

 ans = ["" for _ in arr]

 

 # Store count of each character

 for i in arr:

 count[ord(i)] += 1

 

 # Change count[i] so that count[i] now contains actual

 # position of this character in output array

 for i in range(256):

 count[i] += count[i-1]

 

 # Build the output character array

 for i in range(len(arr)):

 output[count[ord(arr[i])]-1] = arr[i]

 count[ord(arr[i])] -= 1

 

 # Copy the output array to arr, so that arr now

 # contains sorted characters

 for i in range(len(arr)):

 ans[i] = output[i]

 return ans 

 

# Driver program to test above function

arr = "geeksforgeeks"

ans = countSort(arr)

print "Sorted character array is %s" %("".join(ans))

 

# This code is contributed by Nikhil Kumar Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    Sorted character array is eeeefggkkorss
    

Please refer complete article on Counting Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

