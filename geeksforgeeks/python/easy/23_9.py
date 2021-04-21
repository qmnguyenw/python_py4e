Python program to find common elements in three lists using sets



Prerequisite : Sets in Python

Given three arrays, we have to find common elements in three sorted lists
using sets.

Examples :

    
    
    Input : ar1 = [1, 5, 10, 20, 40, 80]
            ar2 = [6, 7, 20, 80, 100]
            ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    
    Output : [80, 20]
    
    Input : ar1 = [1, 5, 5]
            ar2 = [3, 4, 5, 5, 10]
            ar3 = [5, 5, 10, 20]
    
    Output : [5]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :**  
We have given three arrays, with the help of sets one can easily find out the
intersection of these Arrays.

  

  

Intersection method simply provides the intersection of both the arrays upon
which you want to perform the operation of intersection (or, it simply gives
out the common elements in both the array). We will be taking three arrays and
then we will take out the intersection.

Below is the implementation of above approach :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find common elements

# in three lists using sets

 

def IntersecOfSets(arr1, arr2, arr3):

 # Converting the arrays into sets

 s1 = set(arr1)

 s2 = set(arr2)

 s3 = set(arr3)

 

 # Calculates intersection of 

 # sets on s1 and s2

 set1 = s1.intersection(s2) #[80, 20, 100]

 

 # Calculates intersection of sets

 # on set1 and s3

 result_set = set1.intersection(s3)

 

 # Converts resulting set to list

 final_list = list(result_set)

 print(final_list)

 

# Driver Code

if __name__ == '__main__' :

 

 # Elements in Array1

 arr1 = [1, 5, 10, 20, 40, 80, 100]

 

 # Elements in Array2

 arr2 = [6, 7, 20, 80, 100]

 

 # Elements in Array3

 arr3 = [3, 4, 15, 20, 30, 70, 80,
120]

 

 # Calling Function

 IntersecOfSets(arr1, arr2, arr3)  
  
---  
  
 __

 __

Output :

    
    
    [80, 20]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

