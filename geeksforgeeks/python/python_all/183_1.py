Python Program for Odd-Even Sort / Brick Sort



This is basically a variation of bubble-sort. This algorithm is divided into
two phases- Odd and Even Phase. The algorithm runs until the array elements
are sorted and in each iteration two phases occurs- Odd and Even Phases.

In the odd phase, we perform a bubble sort on odd indexed elements and in the
even phase, we perform a bubble sort on even indexed elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to implement

# Odd-Even / Brick Sort

 

def oddEvenSort(arr, n):

 # Initially array is unsorted

 isSorted = 0

 while isSorted == 0:

 isSorted = 1

 temp = 0

 for i in range(1, n-1, 2):

 if arr[i] > arr[i+1]:

 arr[i], arr[i+1] = arr[i+1], arr[i]

 isSorted = 0

 

 for i in range(0, n-1, 2):

 if arr[i] > arr[i+1]:

 arr[i], arr[i+1] = arr[i+1], arr[i]

 isSorted = 0

 

 return

 

 

arr = [34, 2, 10, -9]

n = len(arr)

 

oddEvenSort(arr, n);

for i in range(0, n):

 print(arr[i], end =" ")

 

# Code Contribute by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output :**

    
    
    -9 2 10 34 

Please refer complete article on Odd-Even Sort / Brick Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

