Python Program for Insertion Sort



Insertion sort is a simple sorting algorithm that works the way we sort
playing cards in our hands.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Insertion Sort

 

# Function to do insertion sort

def insertionSort(arr):

 

 # Traverse through 1 to len(arr)

 for i in range(1, len(arr)):

 

 key = arr[i]

 

 # Move elements of arr[0..i-1], that are

 # greater than key, to one position ahead

 # of their current position

 j = i-1

 while j >=0 and key < arr[j] :

 arr[j+1] = arr[j]

 j -= 1

 arr[j+1] = key

 

 

# Driver code to test above

arr = [12, 11, 13, 5, 6]

insertionSort(arr)

print ("Sorted array is:")

for i in range(len(arr)):

 print ("%d" %arr[i])

 

# This code is contributed by Mohit Kumra  
  
---  
  
 __

 __

 **Output:**

    
    
    Sorted array is:
    5
    6
    11
    12
    13
    
    

Please refer complete article on Insertion Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

