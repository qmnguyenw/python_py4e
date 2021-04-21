Python program to find N largest elements from a list



Given a list of integers, the task is to find N largest elements assuming size
of list is greater than or equal o N.

 **Examples :**

    
    
    Input : [4, 5, 1, 2, 9] 
            N = 2
    Output :  [9, 5]
    
    Input : [81, 52, 45, 10, 3, 2, 96] 
            N = 3
    Output : [81, 96, 52]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A simple solution traverse the given list N times. In every traversal, find
the maximum, add it to result, and remove it from the list. Below is the
implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find N largest

# element from given list of integers

 

# Function returns N largest elements

def Nmaxelements(list1, N):

 final_list = []

 

 for i in range(0, N): 

 max1 = 0

 

 for j in range(len(list1)): 

 if list1[j] > max1:

 max1 = list1[j];

 

 list1.remove(max1);

 final_list.append(max1)

 

 print(final_list)

 

# Driver code

list1 = [2, 6, 41, 85, 0, 3, 7, 6,
10]

N = 2

 

# Calling the function

Nmaxelements(list1, N)  
  
---  
  
 __

 __

Output :

    
    
    [85, 41]

Time Complexity : O(N * size) where size is size of the given list.  
Method 2:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find N largest

# element from given list of integers

 

l = [1000,298,3579,100,200,-45,900]

n = 4

 

l.sort()

print(l[-n:])  
  
---  
  
 __

 __

Output:

    
    
    [-45, 100, 200, 298, 900, 1000, 3579]
    Find the N largest element: 4
    [298, 900, 1000, 3579]
    

Please refer k largest(or smallest) elements in an array for more efficient
solutions of this problem.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

