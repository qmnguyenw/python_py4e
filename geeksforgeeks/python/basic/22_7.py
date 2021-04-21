Python program to find Cumulative sum of a list



The problem statement asks to produce a new list whose i^{th} element will be
equal to the sum of the (i + 1) elements.

 **Examples :**  

    
    
    Input : list = [10, 20, 30, 40, 50]
    Output : [10, 30, 60, 100, 150]
    
    Input : list = [4, 10, 15, 18, 20]
    Output : [4, 14, 29, 47, 67]
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach 1 :**  
We will use the concept of list comprehension and list slicing to get the
cumulative sum of the list. The list comprehension has been used to access
each element from the list and slicing has been done to access the elements
from start to the i+1 element. We have used the sum() method to sum up the
elements of the list from start to i+1.  
Below is the implementation of the above approach :  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to get the Cumulative sum of a list

def Cumulative(lists):

 cu_list = []

 length = len(lists)

 cu_list = [sum(lists[0:x:1]) for x in
range(0, length+1)]

 return cu_list[1:]

# Driver Code

lists = [10, 20, 30, 40, 50]

print (Cumulative(lists))  
  
---  
  
 __

 __

 **Output :**  

  

  

    
    
    [10, 30, 60, 100, 150]
    
    

**Approach 2:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

list=[10,20,30,40,50]

new_list=[]

j=0

for i in range(0,len(list)):

 j+=list[i]

 new_list.append(j)

 

print(new_list)

#code given by Divyanshu singh  
  
---  
  
 __

 __

 **Output :**  

    
    
    [10, 30, 60, 100, 150]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

