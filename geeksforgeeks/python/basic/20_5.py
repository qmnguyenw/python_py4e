Python | Program to print duplicates from a list of integers



  
Given a list of integers with duplicate elements in it. The task to generate
another list, which contains only the duplicate elements. In simple words, the
new list should contain the elements which appear more than one.

 **Examples :**

    
    
    Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    Output : output_list = [20, 30, -20, 60]
    
    
    Input :  list = [-1, 1, -1, 8]
    Output : output_list = [-1]
    

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# duplicates from a list 

# of integers

def Repeat(x):

 _size = len(x)

 repeated = []

 for i in range(_size):

 k = i + 1

 for j in range(k, _size):

 if x[i] == x[j] and x[i] not in repeated:

 repeated.append(x[i])

 return repeated

 

# Driver Code

list1 = [10, 20, 30, 20, 20, 30, 40, 

 50, -20, 60, 60, -20, -20]

print (Repeat(list1))

 

# This code is contributed 

# by Sandeep_anand  
  
---  
  
 __

 __

 **Output :**

    
    
    [20, 30, -20, 60]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

