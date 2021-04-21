Python | Program to count number of lists in a list of lists



Given a list of lists, write a Python program to count the number of lists
contained within the list of lists.

 **Examples:**

    
    
    **Input :**  [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    **Output :** 3
    
    **Input :** [[1], ['Bob'], ['Delhi'], ['x', 'y']]
    **Output :** 4
    

  
**Method #1 :** Using _len()_

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Count number

# of lists in a list of lists

 

def countList(lst):

 return len(lst)

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(countList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

  
**Method #2 :** Using _type()_

  

  

Use a for loop and in every iteration to check if the type of the current item
is a list or not, and accordingly increment ‘count’ variable. This method has
a benefit over approach #1, as it works well for a list of heterogeneous
elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Count number

# of lists in a list of lists

 

def countList(lst):

 count = 0

 for el in lst:

 if type(el)== type([]):

 count+= 1

 

 return count

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(countList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

A one-liner alternative approach for the above code is given below:

 __

 __  
 __

 __

 __  
 __  
 __

def countList(lst):

 return sum(type(el)== type([]) for el in lst)  
  
---  
  
 __

 __

  
**Method #3 :** Using _isinstance()_ method

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Count number

# of lists in a list of lists

 

def countList(lst):

 return sum(isinstance(i, list) for i in lst)

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(countList(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

