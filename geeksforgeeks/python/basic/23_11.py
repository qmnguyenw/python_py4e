Python | Difference between two lists



There are various ways in which difference between two lists can be generated.
In this article, we will see two most important ways in which this can be
done. One by using the set() method, and another by not using it.  
Examples:  

    
    
              Input :
    list1 = [10, 15, 20, 25, 30, 35, 40]
    list2 = [25, 40, 35] 
    Output :
    [10, 20, 30, 15]
    Explanation:
    resultant list = list1 - list2
              
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

  1. **By the use of set()**   
In this method we convert the lists into sets explicitly and then simply
reduce one from the other using the subtract operator. For more reference on
set visit Sets in Python.  
Example:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code t get difference of two lists

# Using set()

def Diff(li1, li2):

 return (list(list(set(li1)-set(li2)) +
list(set(li2)-set(li1))))

# Driver Code

li1 = [10, 15, 20, 25, 30, 35, 40]

li2 = [25, 40, 35]

print(Diff(li1, li2))  
  
---  
  
 __

 __

  1. Output :  

    
    
    [10, 20, 30, 15]
    

  1.   2. **Without using the set()**   
In this method, we use the basic combination technique to copy elements from
both the list with a regular check if one is present in the other or not.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code t get difference of two lists

# Not using set()

def Diff(li1, li2):

 li_dif = [i for i in li1 + li2 if i not in li1
or i not in li2]

 return li_dif

# Driver Code

li1 = [10, 15, 20, 25, 30, 35, 40]

li2 = [25, 40, 35]

li3 = Diff(li1, li2)

print(li3)  
  
---  
  
 __

 __

  1. Output :  

    
    
    [10, 20, 30, 15]
    

  1. 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

