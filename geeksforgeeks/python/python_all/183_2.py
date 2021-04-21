Python Program for Gnome Sort



 **Algorithm Steps**

  1. If you are at the start of the array then go to the right element (from arr[0] to arr[1]).
  2. If the current array element is larger or equal to the previous array element then go one step right

    
    
                       if (arr[i] >= arr[i-1])
                          i++;
    

  3. If the current array element is smaller than the previous array element then swap these two elements and go one step backwards

    
    
                           if (arr[i] < arr[i-1])
                           {
                               swap(arr[i], arr[i-1]);
                               i--;
                           }
    

  4. Repeat steps 2) and 3) till ‘i’ reaches the end of the array (i.e- ‘n-1’)
  5. If the end of the array is reached then stop and the array is sorted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to implement Gnome Sort

 

# A function to sort the given list using Gnome sort

def gnomeSort( arr, n):

 index = 0

 while index < n:

 if index == 0:

 index = index + 1

 if arr[index] >= arr[index - 1]:

 index = index + 1

 else:

 arr[index], arr[index-1] = arr[index-1], arr[index]

 index = index - 1

 

 return arr

 

# Driver Code

arr = [ 34, 2, 10, -9]

n = len(arr)

 

arr = gnomeSort(arr, n)

print "Sorted seqquence after applying Gnome Sort :",

for i in arr:

 print i,

 

# Contributed By Harshit Agrawal  
  
---  
  
 __

 __

 **Output:**

    
    
    Sorted seqquence after applying Gnome Sort : -9 2 10 34
    

Please refer complete article on Gnome Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

